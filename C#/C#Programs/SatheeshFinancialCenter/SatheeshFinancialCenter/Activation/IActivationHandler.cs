using System.Threading.Tasks;

namespace SatheeshFinancialCenter.Activation;

public interface IActivationHandler
{
    bool CanHandle(object args);

    Task HandleAsync(object args);
}
