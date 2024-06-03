from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


# Function to create an invoice PDF
def create_invoice(invoice_data):
    # Extract invoice data
    date = invoice_data["date"]
    skus = invoice_data["skus"]
    notes = invoice_data["notes"]
    customer_id = invoice_data["customer"]
    # Get Customer Information
    customer = Customer.objects.get(id=customer_id)
    customer_name = f"{customer.first_name} {customer.last_name}"
    try:
        customer_address = f"{customer.address_1} {customer.address_2}\n{customer.city}, {customer.state} {customer.zip_code}"
    except:
        customer_address = None
    customer_email = customer.email
    # Create a PDF file
    pdf_file = f"invoice_{customer_id}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    # Draw the invoice
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, 10.5 * inch, f"Invoice Date: {date}")
    c.drawString(1 * inch, 10 * inch, f"Customer ID: {customer_id}")
    c.drawString(1 * inch, 9.5 * inch, f"Customer Name: {customer_name}")
    if customer_address is not None:
        c.drawString(1 * inch, 9 * inch, f"Customer Address: {customer_address}")
    c.drawString(1 * inch, 8.5 * inch, f"Customer Email: {customer_email}")
    # Table header
    c.drawString(1 * inch, 6 * inch, "SKU")
    c.drawString(2 * inch, 8 * inch, "Title")
    c.drawString(5 * inch, 6 * inch, "Quantity")
    c.drawString(6 * inch, 6 * inch, "Unit Price")
    c.drawString(7 * inch, 6 * inch, "Total Price")
    # Table content
    y = 7.5 * inch
    total_cost = 0
    for item in skus:
        c.drawString(1 * inch, y, item["sku"])
        c.drawString(3 * inch, y, item["title"])
        c.drawString(5 * inch, y, str(item["quantity"]))
        c.drawString(6 * inch, y, f"${item['salesPrice']:.2f}")
        total_price = item["quantity"] * item["salesPrice"]
        c.drawString(7 * inch, y, f"${total_price:.2f}")
        y -= 0.5 * inch
        total_cost += total_price
    # Total cost
    c.drawString(1 * inch, y, f"Total Cost: ${total_cost:.2f}")
    # Notes
    c.drawString(1 * inch, y - 0.5 * inch, f"Notes: {notes}")
    # Save the PDF
    c.save()
    return pdf_file


# Invoice data
invoice_data = {
    "date": "Sun, 02 Jun 2024 21:43:09 GMT",
    "skus": [
        {
            "sku": "1921DMorBU",
            "cost": 65,
            "title": "1921-D Morgan Silver Dollar BU Raw",
            "quantity": 1,
            "salesPrice": 75,
            "inventoryQuantity": 2400,
        }
    ],
    "notes": "due in 30 days",
    "customer": 22,
}

# Create the invoice PDF
pdf_path = create_invoice(invoice_data)
print(f"Invoice PDF created: {pdf_path}")
