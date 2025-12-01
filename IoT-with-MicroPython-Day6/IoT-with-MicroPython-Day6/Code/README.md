## 🔍 How to View the Data

You can check the database table directly on the Raspberry Pi using the command line.

1.  **Install SQLite3 (if not installed):**
    ```bash
    sudo apt install sqlite3
    ```

2.  **Open the database:**
    ```bash
    sqlite3 iot_data.db
    ```

3.  **View the table structure:**
    ```sql
    .schema sensor_data
    ```

4.  **View the data (after you insert records):**
    To see the data formatted nicely with headers:
    ```sql
    .headers on
    .mode column
    SELECT * FROM sensor_data;
    ```

5.  **Exit the database:**
    ```sql
    .quit
    ```