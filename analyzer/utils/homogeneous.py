"""
analyzer.utils.homogeneous is the homogeneous data converter
which deal with company name via alias table currently.
"""

company_alias = {
    "中國信託": ["中國信託 數據研究發展中心", "中國信託 數研發"],
    "Gogoro": ["gogoro"],
    "Dcard": ["DCard"],
    "天堂遊戲": ["天堂遊戲有限公司", "Paradise-soft"],
    "亞洲指標數位行銷顧問股份有限公司": ["亞洲數位指標顧問股份有限公司", "亞洲指標數位行銷股份有限公司"],
    "MoBagel": ["行動貝果有限公司", "Mobagel"],
    "趨勢科技": ["Trend Micro", "Trendmicro", "TrendMicro"],
    "中央研究院": ["中研院資訊所"],
    "Appier": ["Appier Inc."],
    "InfuseAI": ["InfuseAI Inc."],
    "iCHEF": ["iCHEF 資廚", "IDATA", "ICHEF"],
    "UmboCV": ["Umbo Computer VIsion", "Umbo Computer Vision"],
    "Avnet": ["新加坡商安富利股份有限公司台灣分公司"],
    "塔圖科技股份公司": ["塔圖科技股份有限公司"],
    "HACARUS": ["Hacarus Inc."],
    "國泰金控": [
        "國泰世華銀行/中台發展部",
        "Cathay DDT",
        "Cathay Financial Holdings",
        "Cathayholdings",
    ],
    "Shopee": ["Shopee Taiwan", "樂購蝦皮股份有限公司"],
    "Gemini Data": ["Gemini Data, Engineering"],
    "玉山銀行": ["E.SUN Bank", "E.Sun Bank"],
    "Unnotech": ["創順科技", "創順科技有限公司"],
    "EMQ": ["EMQ Inc."],
}

vacancy_alias = {
    "DevOps": ["DevOp", "Automation"],
    "Fintech": ["Fintech", "Finance"],
    "Embedded": ["Physical"],
    "Quality Assurance": ["Quality", "QA", "Test", "Validation"],
    "Web": ["Back End", "Backend", "Frontend", "Full Stack", "Django", "後端", "前端"],
    "App": ["Application", "iOS"],
    "Cloud": ["雲端"],
    "Consultant": ["Consultant"],
    "Manager": ["經理", "Lead"],
    "Machine Learning": ["機器視覺", "Computer Vision", "Deep Learning"],
    "Data": ["Analyst", "大數據", "分析", "資料", "數據"],
    "AI": ["人工智慧"],
    "Algorithm": ["演算法", "Algorithm"],
    "Researcher": ["Researcher", "R&D", "Research"],
    "Software Engineer": [
        "工程師",
        "程式設計師",
        "Software",
        "ARCHITECT",
        "Architect",
        "Engineer",
        "Developer",
    ],
}


def convert_company_alias(name):
    """
    uniform company name via alias table.
    """
    for company in company_alias:
        if name in company_alias[company]:
            return company
    return name


def convert_vacancy_alias(name):
    """
    uniform vacancy type via alias table.
    """
    for vacancy in vacancy_alias:
        if vacancy in name or any([x in name for x in vacancy_alias[vacancy]]):
            return vacancy
    return "Others"
