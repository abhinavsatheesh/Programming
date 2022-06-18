using System;
using System.Collections.Generic;

namespace SatheeshFinancialCenter.Core.Models;

// Model for the SampleDataService. Replace with your own model.
public class SampleOrder
{
    public string OrderID
    {
        get; set;
    }

    public string OrderDate
    {
        get; set;
    }

    
    public string Company
    {
        get; set;
    }

    

    

    public ICollection<SampleOrderDetail> Details
    {
        get; set;
    }

    public string ShortDescription => $"Order ID: {OrderID}";

    
}
