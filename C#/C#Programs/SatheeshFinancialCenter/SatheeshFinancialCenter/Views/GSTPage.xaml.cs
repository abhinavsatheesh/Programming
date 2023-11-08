using Microsoft.UI.Xaml.Controls;

using SatheeshFinancialCenter.ViewModels;

namespace SatheeshFinancialCenter.Views;

public sealed partial class GSTPage : Page
{
    public GSTViewModel ViewModel
    {
        get;
    }

    public GSTPage()
    {
        ViewModel = App.GetService<GSTViewModel>();
        InitializeComponent();
    }
}
