#!/usr/bin/env python3
"""
TeslaMate Hungarian Translation Generator
Creates Hungarian (hu) translation files for TeslaMate
"""

# Hungarian translations dictionary
TRANSLATIONS = {
    # Main UI
    "Status": "Állapot",
    "Speed": "Sebesség",
    "State of Charge": "Töltöttségi Szint",
    "Charged": "Töltve",
    "asleep": "alszik",
    "charging": "töltés",
    "driving": "vezet",
    "offline": "offline",
    "online": "online",
    "updating": "frissítés",
    "Locked": "Zárva",
    "Sentry Mode": "Őr Mód",
    "Home": "Kezdőlap",
    "Settings": "Beállítások",
    "Scheduled Charging": "Ütemezett Töltés",
    "Plugged In": "Csatlakoztatva",
    "Charge Limit": "Töltési Limit",
    "Battery": "Akkumulátor",
    "Range": "Hatótávolság",
    "Ideal Range": "Ideális Hatótávolság",
    "Rated Range": "Becsült Hatótávolság",
    "Est. Range": "Becs. Hatótávolság",
    "Power": "Teljesítmény",
    "Charger": "Töltő",
    "Charger Power": "Töltő Teljesítmény",
    "Voltage": "Feszültség",
    "Current": "Áramerősség",
    "Time to full": "Idő teli töltésig",
    "Add Energy": "Hozzáadott Energia",
    "Cost": "Költség",
    "Efficiency": "Hatékonyság",
    "Temperature": "Hőmérséklet",
    "Outside": "Kint",
    "Inside": "Bent",
    "Frunk": "Első Csomagtartó",
    "Trunk": "Csomagtartó",
    "Driver": "Vezető",
    "Passenger": "Utas",
    "Rear Left": "Hátsó Bal",
    "Rear Right": "Hátsó Jobb",
    "Windows": "Ablakok",
    "Doors": "Ajtók",
    "Open": "Nyitva",
    "Closed": "Zárva",
    "Location": "Helyszín",
    "Odometer": "Kilométeróra",
    "Firmware": "Firmware",
    "Version": "Verzió",
    "Elevation": "Magasság",
    "Heading": "Irány",
    "Since": "Óta",
    "Position": "Pozíció",
    "Latitude": "Szélesség",
    "Longitude": "Hosszúság",
    "Display Name": "Megjelenítési Név",
    "Vehicle": "Jármű",
    "Car": "Autó",

    # Charges
    "Charges": "Töltések",
    "Date": "Dátum",
    "Start Date": "Kezdés Dátuma",
    "End Date": "Befejezés Dátuma",
    "Duration": "Időtartam",
    "Energy": "Energia",
    "Start %": "Kezdő %",
    "End %": "Végső %",
    "Charge Energy Added": "Hozzáadott Energia",
    "Charger Power": "Töltő Teljesítmény",
    "Address": "Cím",
    "Cost": "Költség",
    "Details": "Részletek",

    # Drives
    "Drives": "Utak",
    "Start": "Kezdés",
    "End": "Befejezés",
    "Distance": "Távolság",
    "Start Address": "Kezdő Cím",
    "End Address": "Végső Cím",
    "Start Range": "Kezdő Hatótávolság",
    "End Range": "Végső Hatótávolság",
    "Start %": "Kezdő %",
    "End %": "Végső %",
    "Used": "Felhasznált",
    "Avg Speed": "Átlagsebesség",
    "Max Speed": "Max Sebesség",
    "Outside Temp Avg": "Külső Hőm. Átlag",
    "Inside Temp Avg": "Belső Hőm. Átlag",

    # Updates
    "Updates": "Frissítések",
    "Update Available": "Frissítés Elérhető",
    "Installing": "Telepítés",
    "Available": "Elérhető",
    "Downloading": "Letöltés",
    "Scheduled": "Ütemezve",

    # Settings
    "Units": "Mértékegységek",
    "Language": "Nyelv",
    "Preferred Range": "Előnyben Részesített Hatótávolság",
    "Length": "Hosszúság",
    "Temperature": "Hőmérséklet",
    "Ideal": "Ideális",
    "Rated": "Becsült",
    "km": "km",
    "mi": "mérföld",
    "kW": "kW",
    "kWh": "kWh",
    "Wh/km": "Wh/km",
    "Wh/mi": "Wh/mérföld",

    # Geofences
    "Geofences": "Geokerítések",
    "New Geofence": "Új Geokerítés",
    "Edit Geofence": "Geokerítés Szerkesztése",
    "Name": "Név",
    "Radius": "Sugár",
    "Latitude": "Szélesség",
    "Longitude": "Hosszúság",
    "Create": "Létrehozás",
    "Update": "Frissítés",
    "Delete": "Törlés",
    "Cancel": "Mégse",
    "Save": "Mentés",

    # Import
    "Import": "Importálás",
    "TeslaFi Import": "TeslaFi Importálás",
    "Select File": "Fájl Kiválasztása",
    "Upload": "Feltöltés",

    # Common
    "yes": "igen",
    "no": "nem",
    "Active": "Aktív",
    "Inactive": "Inaktív",
    "Enabled": "Engedélyezve",
    "Disabled": "Letiltva",
    "Unknown": "Ismeretlen",
    "N/A": "N/A",
    "Loading...": "Betöltés...",
    "Error": "Hiba",
    "Success": "Siker",
    "Warning": "Figyelmeztetés",
    "Info": "Információ",
    "Back": "Vissza",
    "Next": "Következő",
    "Previous": "Előző",
    "First": "Első",
    "Last": "Utolsó",
    "All": "Összes",
    "None": "Nincs",
    "Total": "Összesen",
    "Average": "Átlag",
    "Minimum": "Minimum",
    "Maximum": "Maximum",
    "From": "Ettől",
    "To": "Eddig",
    "at": "helyen",
    "for": "ennyi",
    "ago": "ezelőtt",
    "now": "most",
    "today": "ma",
    "yesterday": "tegnap",
    "hour": "óra",
    "hours": "óra",
    "minute": "perc",
    "minutes": "perc",
    "second": "másodperc",
    "seconds": "másodperc",
    "day": "nap",
    "days": "nap",
    "week": "hét",
    "weeks": "hét",
    "month": "hónap",
    "months": "hónap",
    "year": "év",
    "years": "év",

    # Sign In
    "Sign in": "Bejelentkezés",
    "Sign in to continue": "Jelentkezz be a folytatáshoz",
    "Sign in to your Tesla Account": "Jelentkezz be Tesla fiókodba",
    "Email": "Email",
    "Password": "Jelszó",
    "Sign In": "Bejelentkezés",
    "Sign Out": "Kijelentkezés",
    "You must sign in to access this page.": "Be kell jelentkezned az oldal eléréséhez.",

    # Errors (common)
    "An error occurred": "Hiba történt",
    "Page not found": "Az oldal nem található",
    "Unauthorized": "Nincs jogosultság",
    "Bad request": "Hibás kérés",
    "Internal server error": "Belső szerverhiba",
    "Service unavailable": "A szolgáltatás nem elérhető",

    # Additional missing translations
    "falling asleep": "elalvás",
    "unavailable": "nem elérhető",
    'Geo-fence \\"%{name}\\" created': 'Geokerítés \\"%{name}\\" létrehozva',
    "Geo-Fences": "Geokerítések",
    "Idle Time Before Trying to Sleep": "Várakozási Idő Alvás Előtt",
    "Saving...": "Mentés...",
    "Time to Try Sleeping": "Idő Alvás Megkísérlésére",
    "min": "perc",
    "Signed in successfully": "Sikeres bejelentkezés",
    "Car is unlocked": "Autó feloldva",
    "Preconditioning": "Előkondicionálás",
    "Sentry mode is enabled": "Őr mód bekapcsolva",
    "Driver present": "Vezető jelen van",
    "cancel sleep attempt": "alvás megszakítása",
    "try to sleep": "alvás megkísérlése",
    "Range (est.)": "Hatótávolság (becs.)",
    "Requirements": "Követelmények",
    "Vehicle must be locked": "Járműnek zárva kell lennie",
    "Range (rated)": "Hatótávolság (becsült)",
    "ideal": "ideális",
    "rated": "becsült",
    "Range (ideal)": "Hatótávolság (ideális)",
    "The car's estimate of remaining range is based on a fixed energy consumption in Wh/km. The Wh/km factor is determined by Tesla and is not country specific whereas the rated range is based on regulatory tests in the different markets for that vehicle.": "Az autó becsült hatótávolsága rögzített energiafogyasztáson (Wh/km) alapul. A Wh/km tényezőt a Tesla határozza meg és nem országspecifikus, míg a becsült hatótávolság a jármű különböző piacain végzett szabályozási teszteken alapul.",
    "Update in progress": "Frissítés folyamatban",
    "Windows open": "Ablakok nyitva",
    "Delete '%{geo_fence}'?": "'%{geo_fence}' törlése?",
    "Inside Temperature": "Belső Hőmérséklet",
    "Outside Temperature": "Külső Hőmérséklet",
    "Health check failed": "Állapotellenőrzés sikertelen",
    "Unlocked": "Feloldva",
    "Remaining Time": "Hátralévő Idő",
    "Dashboards": "Dashboard-ok",
    "URLs": "URL-ek",
    "Web App": "Web Alkalmazás",
    "Sleep Mode": "Alvás Mód",
    'Geo-fence \\"%{name}\\" updated': 'Geokerítés \\"%{name}\\" frissítve',
    "Timeout": "Időtúllépés",
    "Reduced Battery Range": "Csökkent Akkumulátor Hatótávolság",
    "≈ %{range} at 100%": "≈ %{range} 100%-nál",
    "Charge Cost": "Töltési Költség",
    "Enter charge cost": "Adja meg a töltési költséget",
    "Saved!": "Mentve!",
    "Fetching vehicle data ...": "Jármű adatainak lekérése ...",
    "Addresses": "Címek",
    "There was a problem retrieving data from OpenStreetMap. Please try again later.": "Hiba történt az OpenStreetMap adatainak lekérésekor. Kérjük, próbálja újra később.",
    "Time zone": "Időzóna",
    "Charge cost": "Töltési költség",
    "Free Supercharging": "Ingyenes Supercharging",
    "General Settings": "Általános Beállítások",
    "Session fee": "Munkamenet díj",
    "Doors open": "Ajtók nyitva",
    "Per kWh": "kWh-nként",
    "Add costs retroactively": "Költségek visszamenőleges hozzáadása",
    "Charging Costs": "Töltési Költségek",
    "Continue": "Folytatás",
    "Mileage": "Futásteljesítmény",
    "Streaming API": "Streaming API",
    "Documentation": "Dokumentáció",
    "GitHub": "GitHub",
    "Update available": "Frissítés elérhető",
    "Doors are open": "Ajtók nyitva vannak",
    "Trunk is open": "Csomagtartó nyitva",
    "Per Minute": "Percenként",
    "Software Update available (%{version})": "Szoftverfrissítés elérhető (%{version})",
    "Sign out": "Kijelentkezés",
    "Access Token": "Hozzáférési Token",
    "Refresh Token": "Frissítő Token",
    "Tokens are invalid": "Token-ek érvénytelenek",
    "Obtaining tokens through the Tesla API requires programming experience or a 3rd-party service. Information can be found %{here}.": "Token-ek megszerzése a Tesla API-n keresztül programozási tapasztalatot vagy harmadik féltől származó szolgáltatást igényel. Információk találhatók %{here}.",
    "here": "itt",
    "Your Tesla account is locked due to too many failed sign in attempts. To unlock your account, reset your password": "Tesla fiókja zárolva van túl sok sikertelen bejelentkezési kísérlet miatt. Fiókja feloldásához állítsa vissza jelszavát",
    "Downloading update": "Frissítés letöltése",
    "No encryption key provided": "Nincs titkosítási kulcs megadva",
    "For more information, see the updated installation guides on %{link}": "További információért lásd a frissített telepítési útmutatót itt: %{link}",
    "The automatically generated encryption key used for the current session can be found <strong>in the application logs</strong>.": "Az aktuális munkamenethez automatikusan generált titkosítási kulcs megtalálható <strong>az alkalmazás naplóiban</strong>.",
    "To ensure that your <strong>Tesla API tokens are stored securely</strong>, an encryption key must be provided to TeslaMate via the <code>ENCRYPTION_KEY</code> environment variable. Otherwise, a <strong>login will be required after every restart</strong>.": "Annak biztosítására, hogy a <strong>Tesla API token-jei biztonságosan legyenek tárolva</strong>, titkosítási kulcsot kell megadni a TeslaMate számára az <code>ENCRYPTION_KEY</code> környezeti változón keresztül. Ellenkező esetben <strong>minden újraindítás után bejelentkezésre lesz szükség</strong>.",
    "Tire Pressure": "Gumiabroncs Nyomás",
    "Dog Mode": "Kutya Mód",
    "Dog mode is enabled": "Kutya mód bekapcsolva",
    "Expected Finish Time": "Várható Befejezési Idő",
    "You are using the API key (%{token}) provided by %{url}. It will allow your TeslaMate to access the official Tesla Fleet API and Tesla Telemetry streaming.": "Az %{url} által biztosított API kulcsot (%{token}) használja. Ez lehetővé teszi TeslaMate számára a hivatalos Tesla Fleet API és Tesla Telemetry streaming elérését.",
    "Data Collection": "Adatgyűjtés",
    "LFP Battery": "LFP Akkumulátor",
    "Sentry Mode recording": "Őr Mód felvétel",
    "View car location on Google Maps": "Autó helyzete Google Maps-en",

    # Ecto/Database error messages
    "can't be blank": "nem lehet üres",
    "has already been taken": "már foglalt",
    "is invalid": "érvénytelen",
    "must be accepted": "el kell fogadni",
    "has invalid format": "érvénytelen formátum",
    "has an invalid entry": "érvénytelen bejegyzés",
    "is reserved": "foglalt",
    "does not match confirmation": "nem egyezik a megerősítéssel",
    "is still associated with this entry": "még mindig kapcsolódik ehhez a bejegyzéshez",
    "are still associated with this entry": "még mindig kapcsolódnak ehhez a bejegyzéshez",
    "must be less than %{number}": "kisebbnek kell lennie, mint %{number}",
    "must be greater than %{number}": "nagyobbnak kell lennie, mint %{number}",
    "must be less than or equal to %{number}": "kisebbnek vagy egyenlőnek kell lennie, mint %{number}",
    "must be greater than or equal to %{number}": "nagyobbnak vagy egyenlőnek kell lennie, mint %{number}",
    "must be equal to %{number}": "egyenlőnek kell lennie ezzel: %{number}",
}

def create_po_file(template_content, output_path, language="hu"):
    """Create a .po file from template with Hungarian translations."""
    lines = []

    # Add header
    lines.append('## `msgid`s in this file come from POT (.pot) files.')
    lines.append('##')
    lines.append('## Do not add, change, or remove `msgid`s manually here as')
    lines.append("## they're tied to the ones in the corresponding POT file")
    lines.append('## (with the same domain).')
    lines.append('##')
    lines.append('## Use `mix gettext.extract --merge` or `mix gettext.merge`')
    lines.append('## to merge POT files into PO files.')
    lines.append('msgid ""')
    lines.append('msgstr ""')
    lines.append(f'"Language: {language}\\n"')
    lines.append('')

    # Process template
    current_msgid = None
    in_plural = False
    comments = []
    skip_header = True  # Skip template header (empty msgid + msgstr)

    for line in template_content.split('\n'):
        if line.startswith('#'):
            if not skip_header:
                comments.append(line)
        elif line.startswith('msgid '):
            # Extract msgid value
            msgid_value = line[6:].strip(' "')

            # Skip the first empty msgid (template header)
            if msgid_value == '' and skip_header:
                continue

            current_msgid = msgid_value
            in_plural = False

            # Write comments
            for comment in comments:
                lines.append(comment)
            comments = []

            lines.append(line)
        elif line.startswith('msgid_plural '):
            # This is a plural form
            in_plural = True
            lines.append(line)
        elif line.startswith('msgstr['):
            # Plural form msgstr - always leave empty
            if in_plural:  # Only write once
                lines.append('msgstr[0] ""')
                lines.append('msgstr[1] ""')
                lines.append('')
                current_msgid = None
                in_plural = False
        elif line.startswith('msgstr '):
            # Skip header msgstr
            if skip_header:
                skip_header = False
                continue

            # Single form msgstr
            if not in_plural:
                # Add translation if available
                if current_msgid and current_msgid in TRANSLATIONS:
                    lines.append(f'msgstr "{TRANSLATIONS[current_msgid]}"')
                else:
                    lines.append('msgstr ""')
                lines.append('')
                current_msgid = None
        elif line.strip() == '':
            lines.append('')

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return len([k for k in TRANSLATIONS if k])

def main():
    import os

    print("TeslaMate Magyar Fordítás Generátor")
    print("=" * 50)
    print()

    # Read local template files
    print("1. Template fájlok olvasása...")
    try:
        with open('priv/gettext/default.pot', 'r', encoding='utf-8') as f:
            default_pot = f.read()
        print("   ✓ default.pot beolvasva")
    except Exception as e:
        print(f"   ✗ Hiba a default.pot olvasásakor: {e}")
        return

    try:
        with open('priv/gettext/errors.pot', 'r', encoding='utf-8') as f:
            errors_pot = f.read()
        print("   ✓ errors.pot beolvasva")
    except Exception as e:
        print(f"   ✗ Hiba az errors.pot olvasásakor: {e}")
        return

    print()
    print("2. Magyar fordítások generálása...")

    # Create output directory
    output_dir = 'priv/gettext/hu/LC_MESSAGES'
    os.makedirs(output_dir, exist_ok=True)

    # Create default.po
    default_po_path = os.path.join(output_dir, 'default.po')
    translated_count = create_po_file(default_pot, default_po_path)
    print(f"   ✓ default.po létrehozva ({translated_count} lefordított string)")

    # Create errors.po
    errors_po_path = os.path.join(output_dir, 'errors.po')
    create_po_file(errors_pot, errors_po_path)
    print(f"   ✓ errors.po létrehozva")

    print()
    print("=" * 50)
    print(f"✓ Magyar fordítás elkészült!")
    print(f"  Mappa: {output_dir}")
    print(f"  Lefordított stringek: {translated_count}")
    print()

if __name__ == '__main__':
    main()
