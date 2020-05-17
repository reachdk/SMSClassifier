
import xml.etree.ElementTree as ET
import pandas as pd

def main():
    tree = ET.parse("Data/sms-20200514205730.xml")
    root = tree.getroot()
    df_cols = ["address", "date", "subject", "body"]
    rows = []

    for node in root:
        s_address = node.attrib.get("address") if node is not None else None
        s_date = node.attrib.get("date") if node is not None else None
        s_subject = node.attrib.get("subject") if node is not None else None
        s_body = node.attrib.get("body") if node is not None else None

        rows.append(tuple((s_address, s_date, s_subject, s_body)))
    out_df = pd.DataFrame(rows, columns=df_cols)


    out_df.to_csv("Data/sms_df.csv", index=False)







if __name__ == '__main__':
    main()