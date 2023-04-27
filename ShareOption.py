# Calculate Relevant Tax on Share Options (RTSO)
import sys

def calculateRTSO(gain):    
    # Calculate tax rates
    income_tax_rate = 0.40
    usc_rate = 0.08
    prsi_rate = 0.04
    
    # Calculate taxes
    income_tax = gain * income_tax_rate
    usc = gain * usc_rate
    prsi = gain * prsi_rate
    
    # Calculate and return RTSO
    rtso = (income_tax + usc + prsi)
    return rtso

# Get command line arguments
strike_price = float(sys.argv[1])
market_value = float(sys.argv[2])
share_count = float(sys.argv[3])

# Calculate income gain
income = float(market_value * share_count)
gain = float(market_value - strike_price)
profit = float(gain * share_count)

# Calculate RTSO
rtso = calculateRTSO(gain)
total_rtso = float((rtso * share_count))

print("Total income from " + str(share_count) + " share sold: €" + str(income))
print("Gross profit: €" + str(profit))
print("Total RTSO owed on profit: €" + str(total_rtso))
print("Net profit: €" + str(profit - total_rtso))
