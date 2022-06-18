using System.Threading.Tasks;

namespace SatheeshFinancialCenter.Contracts.Services;

public interface IActivationService
{
    Task ActivateAsync(object activationArgs);
}
