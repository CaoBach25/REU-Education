using System;
using System.Collections.ObjectModel;
using Xamarin.Forms;

namespace SpaApp
{
    public partial class ServiceDetailPage : ContentPage
    {
        public ObservableCollection<Service> Services { get; set; }

        public ServiceDetailPage(string package)
        {
            InitializeComponent();

            Services = new ObservableCollection<Service>();

            if (package == "Эко")
            {
                Services.Add(new Service { Name = "Сауна", Price = "500₽", Image = "sauna.jpg" });
                Services.Add(new Service { Name = "Бассейн", Price = "700₽", Image = "pool.jpg" });
                Services.Add(new Service { Name = "Расслабляющий массаж", Price = "1000₽", Image = "relax_massage.jpg" });
            }
            else if (package == "Классик")
            {
                Services.Add(new Service { Name = "Глубокий массаж", Price = "1500₽", Image = "deep_massage.jpg" });
                Services.Add(new Service { Name = "Удаление волос", Price = "2000₽", Image = "hair_removal.jpg" });
                Services.Add(new Service { Name = "Базовый уход за кожей", Price = "2500₽", Image = "basic_skincare.jpg" });
            }
            else if (package == "Люкс")
            {
                Services.Add(new Service { Name = "Татуаж бровей", Price = "3000₽", Image = "eyebrow_tattoo.jpg" });
                Services.Add(new Service { Name = "Омоложение кожи", Price = "3500₽", Image = "skin_rejuvenation.jpg" });
                Services.Add(new Service { Name = "Современное отбеливание", Price = "4000₽", Image = "whitening.jpg" });
                Services.Add(new Service { Name = "Детокс-программа", Price = "7000₽", Image = "detox.jpg" });
            }

            BindingContext = this;
        }

        private async void OnServiceSelected(object sender, EventArgs e)
        {
            var button = sender as Button;
            var selectedService = button.CommandParameter as Service;

            await Navigation.PushAsync(new CalendarPage(selectedService));
        }
    }
}
