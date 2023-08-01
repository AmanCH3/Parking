def submit():
    try:
        conn=sqlite3.connect('parking.db')
        c=conn.cursor()
        c.execute("INSERT INTO add_customer VALUES(:full_name,:vehicle_no,:phone_no,:time,:slot_no,:date,:vehicle_type)",{
            "full_name":customer_entry.get(),
            "vehicle_no":vehicle_no_en.get(),
            "phone_no":phone_entry.get(),
            "time":timeentry.get(),
            "slot_no":slot_entry.get(),
            "date":date_entry.get(),
            "vehicle_type":valueinside.get()
            })
        conn.commit()
        conn.close()