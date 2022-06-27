#ifndef DBACCESS_H
#define DBACCESS_H

#include <QtCore>

typedef struct EventData {
    QString summary;
    QDateTime dtstart;
    QDateTime dtend;
    QString location;
    QString description;
    QString calendar;
} EventData;

/*
sqlite> .schema
CREATE TABLE events (UID TEXT, SUMMARY TEXT, DTSTART DATE, DTEND DATE, LOCATION TEXT, DESCRIPTION TEXT, CALENDAR TEXT);
*/

class DBAccess : public QObject {
    Q_OBJECT
public:
    explicit DBAccess(QObject *parent, QString fileName);
    ~DBAccess();

    Q_INVOKABLE QString printOneRow();

    Q_INVOKABLE QList<EventData> getEvents(int count);

private:
    bool createConnection();
    QString m_fileName;
    QString m_connectionName = "";
};

#endif