#include <iostream>
#include <string>
using namespace std;

class Point {
    int x, y;
public:
    void set(int x, int y) {
        this->x = x;
        this->y = y;
    }

    void showPoint() {
        cout << "(" << x << ", " << y << ")" << endl;
    }
};

class Colorpoint : public Point {
    string color;
public:
    void setColor(string color) {
        this->color = color;
    }

    void showColorPoint();
};

void Colorpoint::showColorPoint() {
    cout << color << endl;
    showPoint();
}

int main() {
    Point p;
    Colorpoint cp;

    cp.set(3, 4);
    cp.setColor("red");
    cp.showColorPoint();
}
