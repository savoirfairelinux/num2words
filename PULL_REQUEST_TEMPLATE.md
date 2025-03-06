## Fixes # by Rana Saab (bm-rana)

### Changes proposed in this pull request:

* Handling Rafea and Nasb Cases:

Introduced a rafea parameter to methods like convert, to_currency, to_ordinal, and to_cardinal to control the grammatical case (رفع or نصب).

Updated the process_arabic_group method to properly handle grammatical cases for numbers and their associated words.

Added a change_arabic_word_end method to adjust word endings based on the grammatical case (e.g., converting "اثنا عشر" to "اثني عشر" in the Nasb case).

* Decimal Point Conversion:

Modified decimal_value in lang_AR so that it takes the decimal part as it is with no modifications 

Implemented a convert_fraction_to_text method to handle the conversion of decimal parts into Arabic text (e.g., "جزءاً واحد من المئة").

Updated the extract_integer_and_decimal_parts method to properly extract and process the decimal part of the number.

Ensured that decimal values are correctly converted into fractions (e.g., "اثنا عشر جزءاً من المئة").



### Status

- [X] READY
- [ ] HOLD
- [ ] WIP (Work-In-Progress)

### How to verify this change

1. Test Rafea and Nasb Cases
Verify that the code correctly handles the Rafea (رفع) and Nasb (نصب) grammatical cases for numbers.
```
num_converter = Num2Word_AR()

# Test Rafea case
result_rafea = num_converter.to_cardinal(12, rafea=True)
print(result_rafea)  # Expected: "اثنا عشر"

# Test Nasb case
result_nasb = num_converter.to_cardinal(12, rafea=False)
print(result_nasb)  # Expected: "اثني عشر"
```
2. Test Decimal Point Conversion
Verify that decimal parts are correctly converted into Arabic text (e.g., "جزءاً من المئة").
```
num_converter = Num2Word_AR()

# Test decimal conversion in Rafea case
result_rafea_decimal = num_converter.to_currency(12.345, currency='SR', rafea=True)
print(result_rafea_decimal)  # Expected: "اثنا عشر ريالاً وثلاثمائة وخمسة وأربعون هللة"

# Test decimal conversion in Nasb case
result_nasb_decimal = num_converter.to_currency(12.345, currency='SR', rafea=False)
print(result_nasb_decimal)  # Expected: "اثني عشر ريالاً وثلاثمائة وخمسة وأربعون هللة"
```

### Additional notes

