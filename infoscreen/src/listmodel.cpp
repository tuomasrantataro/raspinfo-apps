#include <QtSql>

#include "listmodel.h"
#include "dbaccess.h"

ListModel::ListModel(QObject *parent)
    : QSqlQueryModel(parent)
{
    roleNamesHash.insert(Qt::UserRole, QByteArray("summary"));
    roleNamesHash.insert(Qt::UserRole +1, QByteArray("eventstart"));
    roleNamesHash.insert(Qt::UserRole +2, QByteArray("eventend"));
    roleNamesHash.insert(Qt::UserRole +3, QByteArray("location"));
    roleNamesHash.insert(Qt::UserRole +4, QByteArray("description"));
    roleNamesHash.insert(Qt::UserRole +5, QByteArray("calendar"));
}

QVariant ListModel::data(const QModelIndex &index, int role) const
{
    if (role < Qt::UserRole) {
        return QSqlQueryModel::data(index, role);
    }

    QSqlRecord r = record(index.row());
    return r.value(role - Qt::UserRole);
}
