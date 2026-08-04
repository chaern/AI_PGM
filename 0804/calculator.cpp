#include <windows.h>
#include <string>

using namespace std;

HWND hDisplay;

double firstNumber = 0;
char operation = 0;
bool newInput = true;

LRESULT CALLBACK WindowProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam);

void AddText(string text)
{
    char buffer[256];
    GetWindowTextA(hDisplay, buffer, 256);

    string current(buffer);

    if (newInput)
    {
        current = "";
        newInput = false;
    }

    current += text;

    SetWindowTextA(hDisplay, current.c_str());
}

double GetNumber()
{
    char buffer[256];
    GetWindowTextA(hDisplay, buffer, 256);

    return atof(buffer);
}

void Calculate()
{
    double second = GetNumber();
    double result = 0;

    switch (operation)
    {
    case '+':
        result = firstNumber + second;
        break;

    case '-':
        result = firstNumber - second;
        break;

    case '*':
        result = firstNumber * second;
        break;

    case '/':
        if (second != 0)
            result = firstNumber / second;
        else
            MessageBoxA(NULL, "0으로 나눌 수 없습니다.", "오류", MB_OK);
        break;
    }

    string text = to_string(result);

    SetWindowTextA(hDisplay, text.c_str());

    newInput = true;
}


int WINAPI WinMain(
    HINSTANCE hInstance,
    HINSTANCE,
    LPSTR,
    int nCmdShow)
{
    WNDCLASS wc = {};

    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = "Calculator";

    RegisterClass(&wc);


    HWND hwnd = CreateWindow(
        "Calculator",
        "C++ 계산기",
        WS_OVERLAPPEDWINDOW,
        500, 200,
        320, 420,
        NULL,
        NULL,
        hInstance,
        NULL
    );


    ShowWindow(hwnd, nCmdShow);


    MSG msg = {};

    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }


    return 0;
}



LRESULT CALLBACK WindowProc(
    HWND hwnd,
    UINT msg,
    WPARAM wParam,
    LPARAM lParam)
{
    switch (msg)
    {
    case WM_CREATE:
    {
        hDisplay = CreateWindow(
            "EDIT",
            "0",
            WS_CHILD | WS_VISIBLE | WS_BORDER | ES_RIGHT,
            20, 20,
            260, 40,
            hwnd,
            NULL,
            NULL,
            NULL
        );


        const char* buttons[4][4] =
        {
            {"7","8","9","/"},
            {"4","5","6","*"},
            {"1","2","3","-"},
            {"0","C","=","+"}
        };


        int id = 1;

        for (int y = 0; y < 4; y++)
        {
            for (int x = 0; x < 4; x++)
            {
                CreateWindow(
                    "BUTTON",
                    buttons[y][x],
                    WS_CHILD | WS_VISIBLE,
                    20 + x * 65,
                    80 + y * 60,
                    55,
                    45,
                    hwnd,
                    (HMENU)id,
                    NULL,
                    NULL
                );

                id++;
            }
        }

        break;
    }


    case WM_COMMAND:
    {
        int id = LOWORD(wParam);

        if (id >= 1 && id <= 16)
        {
            int index = id - 1;

            string keys =
                "789/"
                "456*"
                "123-"
                "0C=+";

            char key = keys[index];


            if (key >= '0' && key <= '9')
            {
                AddText(string(1, key));
            }

            else if (key == 'C')
            {
                SetWindowTextA(hDisplay, "0");
                firstNumber = 0;
                operation = 0;
                newInput = true;
            }

            else if (key == '=')
            {
                Calculate();
            }

            else
            {
                firstNumber = GetNumber();
                operation = key;
                newInput = true;
            }
        }

        break;
    }


    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    }


    return DefWindowProc(hwnd, msg, wParam, lParam);
}