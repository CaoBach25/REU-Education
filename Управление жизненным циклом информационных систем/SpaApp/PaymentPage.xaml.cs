using System;
using Xamarin.Forms;

namespace SpaApp
{
    public partial class PaymentPage : ContentPage
    {
        private Service _selectedService;
        private string _extraParam1;
        private string _extraParam2;

        // Constructor hỗ trợ 3 tham số
        public PaymentPage(Service service, string param1 = null, string param2 = null)
        {
            InitializeComponent();
            _selectedService = service;
            _extraParam1 = param1;
            _extraParam2 = param2;

            // Ví dụ xử lý các tham số bổ sung nếu cần
            if (!string.IsNullOrEmpty(_extraParam1))
            {
                Console.WriteLine($"Received param1: {_extraParam1}");
            }

            if (!string.IsNullOrEmpty(_extraParam2))
            {
                Console.WriteLine($"Received param2: {_extraParam2}");
            }
        }

        private async void OnPayClicked(object sender, EventArgs e)
        {
            string cardNumber = CardNumberEntry.Text;
            string expiryDate = ExpiryDateEntry.Text;
            string cvc = CVCEntry.Text;

            // Kiểm tra thông tin nhập
            if (string.IsNullOrWhiteSpace(cardNumber) || string.IsNullOrWhiteSpace(expiryDate) || string.IsNullOrWhiteSpace(cvc))
            {
                await DisplayAlert("Ошибка", "Заполните все поля.", "OK");
                return;
            }

            if (cardNumber.Length != 16)
            {
                await DisplayAlert("Ошибка", "Номер карты должен содержать 16 цифр.", "OK");
                return;
            }

            // Hiển thị thông báo thanh toán thành công
            PaymentLayout.IsVisible = false;
            SuccessLayout.IsVisible = true;
        }

        private async void OnBackToMainPage(object sender, EventArgs e)
        {
            await Navigation.PopToRootAsync(); // Quay lại trang chính
        }

        private void OnExpiryDateTextChanged(object sender, TextChangedEventArgs e)
        {
            var entry = sender as Entry;

            if (entry.Text.Length == 2 && !entry.Text.Contains("/"))
            {
                entry.Text += "/";
                entry.CursorPosition = entry.Text.Length;
            }
        }
    }
}
