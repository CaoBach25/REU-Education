using System;
using Xamarin.Forms;

namespace SpaApp
{
    public partial class ServicesPage : ContentPage
    {
        public ServicesPage()
        {
            InitializeComponent();
        }

        private async void OnEcoClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new ServiceDetailPage("Эко"));
        }

        private async void OnClassicClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new ServiceDetailPage("Классик"));
        }

        private async void OnLuxuryClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new ServiceDetailPage("Люкс"));
        }
    }
}
