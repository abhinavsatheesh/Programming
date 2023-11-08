using Microsoft.UI.Xaml.Controls;

using SatheeshFinancialCenter.ViewModels;

namespace SatheeshFinancialCenter.Views;

// TODO: Change the grid as appropriate for your app. Adjust the column definitions on DataGridPage.xaml.
// For more details, see the documentation at https://docs.microsoft.com/windows/communitytoolkit/controls/datagrid.
public sealed partial class IncomeTaxPage : Page
{
    public IncomeTaxViewModel ViewModel
    {
        get;
    }

    public IncomeTaxPage()
    {
        ViewModel = App.GetService<IncomeTaxViewModel>();
        InitializeComponent();
    }
}
