#include <iostream>
using namespace std;

// Định nghĩa cấu trúc Node để tạo ra từng nút trong danh sách
struct Node {
    int data;       // Dữ liệu của nút (ở đây là một số nguyên)
    Node* next;     // Con trỏ trỏ tới nút kế tiếp trong danh sách

    Node(int value) : data(value), next(nullptr) {} // Hàm khởi tạo để gán giá trị và đặt next là nullptr
};

// Hàm để thêm một nút mới vào đầu danh sách
void addToHead(Node*& head, int value) {
    // Tạo một nút mới với giá trị 'value'
    Node* newNode = new Node(value);
    // Cho nút mới trỏ tới nút hiện tại là đầu danh sách
    newNode->next = head;
    // Cập nhật nút đầu tiên của danh sách thành nút mới
    head = newNode;
}

// Hàm để in toàn bộ danh sách ra màn hình
void printList(Node* head) {
    Node* current = head; // Bắt đầu từ đầu danh sách
    while (current != nullptr) { // Lặp qua từng nút cho đến khi gặp nullptr
        cout << current->data << " -> "; // In giá trị của nút
        current = current->next; // Chuyển sang nút tiếp theo
    }
    cout << "nullptr" << endl; // Kết thúc danh sách với nullptr
}

// Hàm tách danh sách thành hai danh sách: L1 (dương) và L2 (còn lại)
void splitList(Node* L, Node*& L1, Node*& L2) {
    Node* current = L; // Bắt đầu từ đầu danh sách gốc
    while (current != nullptr) {
        if (current->data > 0) {
            addToHead(L1, current->data);  // Thêm vào L1 nếu giá trị dương
        } else {
            addToHead(L2, current->data);  // Thêm vào L2 nếu giá trị âm hoặc bằng 0
        }
        current = current->next; // Chuyển sang nút tiếp theo
    }
}

// Hàm để xóa các phần tử âm khỏi danh sách
void removeNegatives(Node*& head) {
    Node* current = head; // Bắt đầu từ đầu danh sách
    Node* prev = nullptr; // Con trỏ lưu nút trước đó

    while (current != nullptr) {
        if (current->data < 0) {  // Nếu giá trị âm
            if (prev == nullptr) { // Nếu là nút đầu danh sách
                head = current->next; // Cập nhật đầu danh sách
            } else {
                prev->next = current->next; // Bỏ qua nút hiện tại
            }
            Node* toDelete = current; // Lưu nút cần xóa
            current = current->next; // Chuyển sang nút tiếp theo
            delete toDelete; // Giải phóng bộ nhớ của nút cần xóa
        } else {
            prev = current; // Cập nhật prev nếu không xóa nút
            current = current->next; // Chuyển sang nút tiếp theo
        }
    }
}

int main() {
    Node* L = nullptr; // Tạo danh sách rỗng
    addToHead(L, -5);
    addToHead(L, 2);
    addToHead(L, -3);
    addToHead(L, 4);
    addToHead(L, -1);
    addToHead(L, 3);

    cout << "Danh sách L ban đầu: ";
    printList(L);

    Node* L1 = nullptr; // Danh sách các giá trị dương
    Node* L2 = nullptr; // Danh sách các giá trị âm và 0
    splitList(L, L1, L2); // Tách danh sách L thành L1 và L2

    cout << "Danh sách L1 (dương): ";
    printList(L1);

    cout << "Danh sách L2 (âm và 0): ";
    printList(L2);

    removeNegatives(L2); // Xóa phần tử âm khỏi L2
    cout << "Danh sách L2 sau khi xóa phần tử âm: ";
    printList(L2);

    return 0;
}