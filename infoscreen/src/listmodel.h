#ifndef LISTMODEL_H
#define LISTMODEL_H

#include <QSqlQueryModel>

class ListModel : public QSqlQueryModel
{
    Q_OBJECT
public:
    explicit ListModel(QObject *parent = 0);

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const;

protected:
    QHash<int, QByteArray> roleNames() const { return roleNamesHash; }

private:
    QHash<int, QByteArray> roleNamesHash;

};

#endif