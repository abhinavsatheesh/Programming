using Microsoft.UI.Xaml.Controls;

using SatheeshFinancialCenter.ViewModels;

namespace SatheeshFinancialCenter.Views;

public sealed partial class AccountancyPage : Page
{
    public AccountancyViewModel ViewModel
    {
        get;
    }

    public AccountancyPage()
    {
        ViewModel = App.GetService<AccountancyViewModel>();
        InitializeComponent();
    }
}
