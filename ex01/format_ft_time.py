from datetime import datetime
date_now = datetime.now()

seconds_since_1970 = date_now.timestamp()

# Salida en el formato indicado en el script:
print(
    f"Seconds since January 1, 1970: {seconds_since_1970:,.4f} "
    f"or {seconds_since_1970:.2e} in scientific notation"
    )

print(f"{date_now.strftime('%b %d %Y')}")
