using System.Collections.ObjectModel;

using CommunityToolkit.Mvvm.ComponentModel;

using SatheeshFinancialCenter.Contracts.ViewModels;
using SatheeshFinancialCenter.Core.Contracts.Services;
using SatheeshFinancialCenter.Core.Models;

namespace SatheeshFinancialCenter.ViewModels;

public class IncomeTaxViewModel : ObservableRecipient, INavigationAware
{
    private readonly ISampleDataService _sampleDataService;

    public ObservableCollection<SampleOrder> Source { get; } = new ObservableCollection<SampleOrder>();

    public IncomeTaxViewModel(ISampleDataService sampleDataService)
    {
        _sampleDataService = sampleDataService;
    }

    public async void OnNavigatedTo(object parameter)
    {
        Source.Clear();

        // TODO: Replace with real data.
        var data = await _sampleDataService.GetGridDataAsync();

        foreach (var item in data)
        {
            Source.Add(item);
        }
    }

    public void OnNavigatedFrom()
    {
    }
}
