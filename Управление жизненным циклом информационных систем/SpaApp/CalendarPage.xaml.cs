using System;
using System.Collections.ObjectModel;
using Xamarin.Forms;

namespace SpaApp
{
    public partial class CalendarPage : ContentPage
    {
        public ObservableCollection<string> AvailableTimes { get; set; }
        private Service _selectedService;

        public CalendarPage(Service selectedService)
        {
            InitializeComponent();

            _selectedService = selectedService; // Lưu trữ dịch vụ được chọn

            AvailableTimes = new ObservableCollection<string>
            {
                "09:00", "10:00", "11:00", "13:00", "14:00", "15:00", "16:00"
            };

            BindingContext = this;
        }

        private async void OnConfirmDateTimeClicked(object sender, EventArgs e)
        {
            var selectedDate = DatePickerControl.Date.ToString("dd/MM/yyyy"); // Chuyển DateTime thành chuỗi
            var selectedTime = TimePickerControl.SelectedItem?.ToString();

            if (string.IsNullOrEmpty(selectedTime))
            {
                await DisplayAlert("Ошибка", "Выберите время!", "OK");
                return;
            }

            // Chuyển sang trang thanh toán
            await Navigation.PushAsync(new PaymentPage(_selectedService, selectedDate, selectedTime));
        }
    }
}
