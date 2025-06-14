using Xamarin.Forms;

namespace SpaApp
{
    public class NumericValidationBehavior : Behavior<Entry>
    {
        public int MaxLength { get; set; }

        protected override void OnAttachedTo(Entry bindable)
        {
            bindable.TextChanged += OnTextChanged;
            base.OnAttachedTo(bindable);
        }

        protected override void OnDetachingFrom(Entry bindable)
        {
            bindable.TextChanged -= OnTextChanged;
            base.OnDetachingFrom(bindable);
        }

        private void OnTextChanged(object sender, TextChangedEventArgs e)
        {
            var entry = sender as Entry;

            if (entry.Text.Length > MaxLength)
            {
                entry.Text = entry.Text.Substring(0, MaxLength);
            }
        }
    }
}
