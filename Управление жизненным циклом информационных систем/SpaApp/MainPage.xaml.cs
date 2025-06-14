using System;
using Xamarin.Forms;

namespace SpaApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private async void OnRegisterClicked(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(FullNameEntry.Text) ||
                string.IsNullOrWhiteSpace(PhoneEntry.Text) ||
                string.IsNullOrWhiteSpace(EmailEntry.Text))
            {
                await DisplayAlert("Ошибка", "Пожалуйста, заполните все поля.", "OK");
                return;
            }

            // Lưu thông tin khách hàng nếu cần (chưa làm tính năng này).
            string fullName = FullNameEntry.Text;
            string phone = PhoneEntry.Text;
            string email = EmailEntry.Text;

            // Chuyển đến trang chọn gói dịch vụ
            await Navigation.PushAsync(new ServicesPage());
        }
    }
}
