#include "dbaccess.h"

#include <QtSql>
//#include <QDateTime>

DBAccess::DBAccess(QObject *parent, QString filePath)
    : QObject(parent), m_fileName(filePath)
{
    //m_fileName = filePath;

    if (!createConnection()) {
        qWarning() << "Database connection failed. Is this file path correct:" << m_fileName;
        return;
    }
}

DBAccess::~DBAccess()
{
    return;
}

bool DBAccess::createConnection()
{
    auto db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName(m_fileName);

    if (!db.open()) {
        return false;
    }
    else {
        m_connectionName = db.connectionName();
        return true;
    }
}

QString DBAccess::printOneRow()
{
    if (m_connectionName == "") {
        return QString();
    }
    
    QSqlQuery query;
    query.prepare("SELECT summary FROM events WHERE UID=:UID;");
    query.bindValue(":UID", "20230624_hccp4ua6g4r8b10mpvumbibac4@google.com");
    query.exec();

    query.next();

    if (query.isValid()) {
        QString summary = query.value(0).toString();
        return summary;
    }
    else {
        return QString("Failed to get event summary");
    }
}

QList<EventData> DBAccess::getEvents(int count)
{
    if (m_connectionName == "") {
        EventData ev;
        ev.summary = "Database connection failed.";
        QList<EventData> ret = { ev };
        return ret;
    }
    
    QSqlQuery query;
    query.prepare("SELECT summary, dtstart, dtend, location, description, calendar FROM events ORDER BY dtstart");
    query.exec();

    query.next();

    QList<EventData> ret;

    while (query.isValid() && count-- > 0) {
        EventData ev = {
            query.value(0).toString(),
            QDateTime::fromString(query.value(1).toString(), Qt::ISODate),
            QDateTime::fromString(query.value(2).toString(), Qt::ISODate),
            query.value(3).toString(),
            query.value(4).toString(),
            query.value(5).toString()
        };
        ret.append(ev);

        query.next();
        
    }
    return ret;
}