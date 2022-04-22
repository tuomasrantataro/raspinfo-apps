
#include <QTextStream>

int main(int argc, char *argv[])
{
    QTextStream(stdout) << "Running simple_qt with " << argc << " parameters:" << endl;
    for (int i = 0; i < argc; ++i) {
        QTextStream(stdout) << "\t" << argv[i] << endl;
    }

    return 0;
}