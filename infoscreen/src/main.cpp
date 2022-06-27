#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>

#include "dbaccess.h"
#include "listmodel.h"


int main(int argc, char *argv[])
{
    QGuiApplication::setApplicationName("InfoScreen");
    QGuiApplication app(argc, argv);

    QCommandLineParser parser;
    parser.addHelpOption();
    parser.addVersionOption();
    
    QCommandLineOption setConfigFile({ "c", "config-file" }, "Use config file in given location.", "configfile");
    parser.addOption(setConfigFile);

    parser.process(app);

    QString configPath = "config.JSON";


    if (parser.isSet(setConfigFile)) {
        configPath = parser.value(setConfigFile);
        qDebug() << "config file given as parameter:" << configPath;
    }

    QString db_path;

    QJsonObject values;
    QJsonDocument loadDoc;

    QFile loadFile(configPath);

    if (loadFile.open(QIODevice::ReadOnly)) {
        QString settingsData = loadFile.readAll();
        loadDoc = QJsonDocument::fromJson(settingsData.toUtf8());
    }

    if (loadDoc.isObject()) {
        values = loadDoc.object();
    }

    if (!values.value("db_path").isUndefined()) {
        db_path = values["db_path"].toString();
        qDebug() << "new db path set:" << db_path;
    }

    QQmlApplicationEngine engine;

    DBAccess database = DBAccess(&app, db_path);

    ListModel *model = new ListModel();
    model->setQuery("SELECT summary, dtstart, dtend, location, description, calendar FROM events ORDER BY dtstart");

    engine.rootContext()->setContextProperty("database", &database);
    engine.rootContext()->setContextProperty("listmodel", model);

    engine.load(QUrl("qrc:/InfoScreen.qml"));
    if (engine.rootObjects().isEmpty()) {
        return -1;
    }

    return app.exec();
}