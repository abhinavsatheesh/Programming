using System;
using System.Threading.Tasks;

using Microsoft.UI.Xaml;

using SatheeshFinancialCenter.Contracts.Services;
using SatheeshFinancialCenter.ViewModels;

namespace SatheeshFinancialCenter.Activation;

public class DefaultActivationHandler : ActivationHandler<LaunchActivatedEventArgs>
{
    private readonly INavigationService _navigationService;

    public DefaultActivationHandler(INavigationService navigationService)
    {
        _navigationService = navigationService;
    }

    protected override bool CanHandleInternal(LaunchActivatedEventArgs args)
    {
        // None of the ActivationHandlers has handled the activation.
        return _navigationService.Frame.Content == null;
    }

    protected async override Task HandleInternalAsync(LaunchActivatedEventArgs args)
    {
        _navigationService.NavigateTo(typeof(HomeViewModel).FullName, args.Arguments);

        await Task.CompletedTask;
    }
}
