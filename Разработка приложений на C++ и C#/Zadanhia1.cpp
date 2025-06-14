#include <iostream>
using namespace std;

int main() {
    int m;
    cout << "Введите размер матрицы (m): ";
    cin >> m; 
    
    int a[m];
    cout << "Введите " << m << " элементов массива a: ";
    for (int i = 0; i < m; i++) {  
        cin >> a[i];  
    }
    
    int matrix[m][m];
    cout << "Введите элементы матрицы " << m << "*" << m << ":" << endl;
    for (int i = 0; i < m; i++) {      
        for (int j = 0; j < m; j++) {   
            cin >> matrix[i][j];  
        }
    }
    
    for (int i = 0; i < m; i++) {   
        if (a[i] > 0) {   
            for (int j = 0; j < m; j++) {  
                if (matrix[i][j] > 0) {
                    matrix[i][j] = 1; 
                } else if (matrix[i][j] < 0) {
                    matrix[i][j] = -1; 
                }
            }
        }
    }
    cout << "Изменённая матрица:" << endl;
    for (int i = 0; i < m; i++) {       
        for (int j = 0; j < m; j++) {    
            cout << matrix[i][j] << " ";  
        }
        cout << endl; 
    }
    return 0;
}