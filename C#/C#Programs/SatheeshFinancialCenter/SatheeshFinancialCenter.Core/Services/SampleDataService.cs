using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using SatheeshFinancialCenter.Core.Contracts.Services;
using SatheeshFinancialCenter.Core.Models;

namespace SatheeshFinancialCenter.Core.Services;

// This class holds sample data used by some generated pages to show how they can be used.
// TODO: The following classes have been created to display sample data. Delete these files once your app is using real data.
// 1. Contracts/Services/ISampleDataService.cs
// 2. Services/SampleDataService.cs
// 3. Models/SampleCompany.cs
// 4. Models/SampleOrder.cs
// 5. Models/SampleOrderDetail.cs
public class SampleDataService : ISampleDataService
{
    private List<SampleOrder> _allOrders;

    public SampleDataService()
    {
    }

    private static IEnumerable<SampleOrder> AllOrders()
    {
        // The following is order summary data
        var companies = AllCompanies();
        return companies.SelectMany(c => c.Orders);
    }

    private static IEnumerable<SampleCompany> AllCompanies()
    {
        return new List<SampleCompany>()
        {
            new SampleCompany()
            {
                
                Orders = new List<SampleOrder>()
                {
                    new SampleOrder()
                    {
                        OrderID = "₹0 - ₹2,50,000", // Symbol Globe
                        OrderDate = "Nil",
                        Company = "Nil"
                    },
                    new SampleOrder()
                    {
                        OrderID = "₹2,50,001 - ₹ 5,00,000", // Symbol Music
                        OrderDate = "5%",
                        Company = "5%",
                    },
                    new SampleOrder()
                    {
                        OrderID = "₹5,00,001 - ₹ 7,50,000", // Symbol Calendar
                        OrderDate = "₹12500 + 10% of total income exceeding ₹5,00,000",
                        Company = "₹12500 + 20% of total income exceeding ₹5,00,000",
                    }
                }
            },
            new SampleCompany()
            {
                Orders = new List<SampleOrder>()
                {
                    new SampleOrder()
                    {
                        OrderID = "₹7,50,001 - ₹ 10,00,000", // Symbol Camera
                        OrderDate = "₹37500 + 15% of total income exceeding ₹7,50,000",
                        Company = "₹62500 + 20% of total income exceeding ₹7,50,000",
                    },
                    new SampleOrder()
                    {
                        OrderID = "₹10,00,001 - ₹12,50,000", // Symbol Clock
                        OrderDate = "₹75000 + 20% of total income exceeding ₹10,00,000",
                        Company = "₹112500 + 30% of total income exceeding ₹10,00,000",
                    }
                }
            },
            new SampleCompany()
            {
                
                Orders = new List<SampleOrder>()
                {
                    new SampleOrder()
                    {
                        OrderID = "₹12,50,001 - ₹15,00,000", // Symbol Contact
                        OrderDate = "₹125000 + 25% of total income exceeding ₹12,50,000",
                        Company = "₹187500 + 30% of total income exceeding ₹12,50,000",
                    },
                    new SampleOrder()
                    {
                        OrderID = "Above ₹ 15,00,000", // Symbol Star
                        OrderDate = "₹187500 + 30% of total income exceeding ₹15,00,000",
                        Company = "₹262500 + 30% of total income exceeding ₹15,00,000",
                        
                    }
                }
            }
        };
    }

    public async Task<IEnumerable<SampleOrder>> GetGridDataAsync()
    {
        if (_allOrders == null)
        {
            _allOrders = new List<SampleOrder>(AllOrders());
        }

        await Task.CompletedTask;
        return _allOrders;
    }
}
