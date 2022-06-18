using Microsoft.UI.Xaml.Controls;

using SatheeshFinancialCenter.ViewModels;

namespace SatheeshFinancialCenter.Views;

public sealed partial class HomePage : Page
{
    public HomeViewModel ViewModel
    {
        get;
    }

    public HomePage()
    {
        ViewModel = App.GetService<HomeViewModel>();
        InitializeComponent();
    }

    private void Button_Click(object sender, Microsoft.UI.Xaml.RoutedEventArgs e)
    {

    }
}
