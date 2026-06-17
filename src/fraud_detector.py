def detect_fraud(df):
    print("جاري تحليل المعاملات...")
    # قاعدة بسيطة: أي معاملة أكبر من 1000 تعتبر مشبوهة
    suspicious = df[df['amount'] > 1000]
    return suspicious