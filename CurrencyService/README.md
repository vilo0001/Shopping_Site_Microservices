# Currency Service

A Flask-based microservice for currency conversion operations.

## Description

This service provides currency conversion functionality with support for USD, EUR, and DKK (Danish Krone). It uses fixed exchange rates and converts all currencies through USD as the base currency.

## Endpoints

### POST /convert

Converts an amount from one currency to another.

**URL:** `http://localhost:5002/convert`

**Method:** `POST`

**Content-Type:** `application/json`

#### Request Payload

```json
{
  "amount": 100.0,
  "from_currency": "USD",
  "to_currency": "EUR"
}
```

**Parameters:**
- `amount` (number, required): The amount to convert
- `from_currency` (string, required): Source currency code (USD, EUR, DKK)
- `to_currency` (string, required): Target currency code (USD, EUR, DKK)

#### Response

**Success Response (200 OK):**

```json
{
  "original_amount": 100.0,
  "from_currency": "USD",
  "to_currency": "EUR",
  "converted_amount": 85.0,
  "exchange_rate": 0.85
}
```

**Response Fields:**
- `original_amount`: The input amount
- `from_currency`: Source currency code
- `to_currency`: Target currency code
- `converted_amount`: The converted amount (rounded to 2 decimal places)
- `exchange_rate`: The exchange rate used for conversion (rounded to 4 decimal places)

## Supported Currencies

| Currency | Code | Rate (to USD) |
|----------|------|---------------|
| US Dollar | USD | 1.0 |
| Euro | EUR | 0.85 |
| Danish Krone | DKK | 6.37 |

## Running the Service

```bash
python app.py
```

The service will start on port 5002.

## Example Usage

```bash
curl -X POST http://localhost:5002/convert \
  -H "Content-Type: application/json" \
  -d '{"amount": 100, "from_currency": "USD", "to_currency": "EUR"}'
```