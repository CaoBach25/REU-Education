using Xamarin.Forms;

namespace SpaApp
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            // Đặt MainPage làm trang chính
            MainPage = new NavigationPage(new MainPage());
        }

        protected override void OnStart() { }
        protected override void OnSleep() { }
        protected override void OnResume() { }
    }
}
