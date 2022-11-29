import time
from playwright.sync_api import Playwright, sync_playwright, expect
import ddddocr
from PIL import Image
from lxml import etree
import re

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cgifederal.secure.force.com/SiteLogin?",wait_until="networkidle")
    page.get_by_label("电子邮件").click()
    page.get_by_label("电子邮件").click()
    page.get_by_label("电子邮件").fill("xxxxx")
    page.get_by_label("密码").click()
    page.get_by_label("密码").fill("xxxxxx")
    page.get_by_label("*我已经阅读并理解 隐私政策").check()
    page.get_by_role("img").first.screenshot(path="login.png")


    # 验证码图像识别
    im1 = Image.open("login.png")
    # 为了使图片的识别率更高，可以处理一下图片
    imRGBA = im1.convert("RGBA")
    imL = imRGBA.convert("L")
    imL.save("loginRGB.png")
    ocr = ddddocr.DdddOcr()
    with open('loginRGB.png', 'rb') as f:
        img_bytes = f.read()
    text = ocr.classification(img_bytes)
    print("登录验证码为{}".format(text))
    page.locator(
        "[id=\"loginPage\\:SiteTemplate\\:siteLogin\\:loginComponent\\:loginForm\\:recaptcha_response_field\"]").click()
    page.locator(
        "[id=\"loginPage\\:SiteTemplate\\:siteLogin\\:loginComponent\\:loginForm\\:recaptcha_response_field\"]").fill(
        text)

    page.get_by_role("button", name="登陆").click()
    page.wait_for_load_state('networkidle')
    page.goto("https://cgifederal.secure.force.com/applicanthome")
    page.wait_for_load_state('networkidle')
    page.goto("https://cgifederal.secure.force.com/selectvisatype")
    page.wait_for_load_state('networkidle')
    page.get_by_role("button", name="继续").click()
    page.get_by_text("BEIJING (北京)").click()
    page.get_by_role("button", name="继续").click()
    page.get_by_label("商务、旅游和其它签证类型  \n商务旅游签证(B1/B2): B-1类签证适用于商务短期逗留美国的人，而B-2类签证适用于旅游或探亲。大部分申请B-1或B-2类的申请人都会获签一张B-1/B-2的组合签证。").check()
    page.get_by_role("button", name="继续").click()
    page.get_by_role("cell", name="商务旅游签证 B-1/B-2商务旅游签证主要面向短期商务旅行(B-1)或旅游观光/寻求医疗服务(B-2)的申请人。一般而言，B-1签证颁发给赴美从事短期商务活动(同商业伙伴协商)、参加科技/教育/专业/商务领域的会议、处置房产或洽谈合同的申请人。B-2签证颁发给赴美休闲/娱乐的申请人，包括旅游观光、探亲访友、医疗以及其他联谊、社交或服务性质的活动。B-1和B-2签证通常会合二为一，作为一类签证颁发： B-1/B-2。 B1 - 商务旅行 B1/B2 - 商务旅行和旅游观光 B2 - 旅游观光或医疗 过境 外国公民须持有效过境签证才能经美国境内立即继续转往其他国家。此项规定也有例外情况，比如有些游客适用豁免签证计划，无需签证即可在美国过境，还有一些游客的所在国政府与美国达成协议，允许其国民在无签证的情况下赴美旅游。 条约商人或投资者 条约商人（E-1）或条约投资者（E-2）签证适用于来自与美国保持贸易和航海条约的国家的商人或投资者，赴美开展主要在美国和条约国之间的实质性贸易，包括服务性贸易和技术性贸易，或开发和指导国家（该商人/投资者所）投资企业的运作，或根据移民和国籍法案规定，正在进行数额较大的投资。 澳大利亚工作者 - 专业人士 E-3签证仅适用于澳大利亚的国民以及他们的配偶和子女。E-3签证的主申请人在美国只能从事专业职业。配偶及子女不必是澳大利亚公民。尽管如此，在移民申请中，美国不承认事实婚姻关系或同性公民伴侣，如果要符合配偶申请人条件，您需要从出生，死亡和婚姻登记机构（署）获得结婚证书。 新闻工作者 媒体类非移民签证(I)主要面向总部在美国境外的媒体，以满足其代表短期赴美工作的需求。根据美国移民法，外国政府对美国公民办理入境签证的流程和费用作出相关规定，美国政府也将据此采取同等政策，这就是所谓的“互惠”原则。因此，向特定国家的媒体代表提供媒体签证的流程和费用将视签证申请人的本国政府是否为美国媒体代表提供同等便利或互惠措施而定。 北美自由贸易协定专业人员：墨西哥，加拿大 北美自由贸易协定（NAFTA）为美国，加拿大和墨西哥创造了特殊的经济和贸易关系。非移民的北美自由贸易协定专业人员（TN）签证，允许加拿大和墨西哥公民作为北美自由贸易协定专业人员在美国工作，从事美国或外国雇主预先安排的商业活动。永久居民，包括加拿大永久居民，不能作为北美自由贸易区的专业人员从事工作。 北马里亚纳群岛（CNMI）联邦签证 这些签证仅适用于已经在北马里亚纳群岛联邦工作和生活的人。签证类别为“过渡性工作者”（CW-1）签证和长期投资人（E-2C）签证，有效期至2019年12月31日。这两种类型的签证只能在雇用申请书递交至美国公民及移民事务署（USCIS）并经其批准后才能签发。过渡工作者和投资者签证只在进入北马里亚纳群岛联邦（CNMI）时有效。签证持有者不能用此类型签证过境、前往美国或在美国境内任何其它地方工作。但是，菲律宾过渡工作者签证持有人可通过关岛过境进入北马里亚纳群岛。 人口贩卖受害者 贩运人口，也被称为贩卖人口，是现代奴隶制的一种形式，人贩以虚假的就业和更好生活的承诺引诱受害者。美国移民法规定的人口贩卖受害者（T类型）非移民签证，为人口贩卖受害人提供了救援。此签证类别允许人口贩卖受害者留在美国协助调查或起诉贩卖人口违法人。 犯罪活动的受害者 在美国发生或违反美国法律的某些犯罪活动的受害者,可能有资格向美国公民及移民事务署（USCIS）申请U类型非移民签证。受害人必须是由于犯罪活动而遭受重大精神或身体虐待，并掌握有关的犯罪活动信息。执法部门还必须证明受害人已经，正在或者可能对犯罪活动的调查或起诉提供帮助。 外交官和外国政府官员 如果您是A-1，A-2或G-1至G-4签证申请人的随从，佣人，或个体员工，您可以申请相应的A-3或G-5签证。您必须证明自己有资格申请A-3或G-5签证（例如，前雇主的推荐信，以前在这一领域工作的证明等）。领事官员必须有正式的职位，并且双方有意建立（或保持）雇佣关系。此外，外交官（A3）和国际组织雇员（G5）的外籍家庭佣工，在申请签证前必须先在国务院办公室的外国代表团信息管理系统(TOMIS)中注册。有关在信息管理系统TOMIS注册的详细信息，请联系国务院办公室外国代表团管理处。").get_by_role("cell", name="B1/B2 - 商务旅行和旅游观光").locator("#selectedVisaClass").check()
    page.get_by_role("button", name="继续").click()
    page.get_by_role("button", name="继续").click()
    page.get_by_role("button", name="继续").click()
    page.get_by_role("button", name="确认").click()
    page.get_by_role("dialog", name="付款选项").locator("button").click()
    page.get_by_role("button", name="继续").click()

    page.wait_for_load_state('networkidle')
    # 获取预约验证码
    page.locator("[id=\"thePage\\:SiteTemplate\\:recaptcha_form\\:captcha_image\"]").first.screenshot(path="appointment.png")

    # 验证码图像识别
    im1 = Image.open("appointment.png")
    # 为了使图片的识别率更高，可以处理一下图片
    imRGBA = im1.convert("RGBA")
    imL = imRGBA.convert("L")
    imL.save("appointmentRGB.png")
    ocr = ddddocr.DdddOcr()
    with open('appointmentRGB.png', 'rb') as f:
        img_bytes = f.read()
    appointmenttext = ocr.classification(img_bytes)
    print("预约验证码为{}".format(appointmenttext))
    page.locator("[id=\"thePage\\:SiteTemplate\\:recaptcha_form\\:recaptcha_response_field\"]").fill(appointmenttext)
    page.get_by_role("button", name="提交").click()
    page.wait_for_load_state('networkidle')
    html = page.content()


    # 解析可用日期
    data = re.findall("myDayHash\['(.*)'] = true", string=html)
    print(data)

    #解析可用时间
    html = etree.HTML(html)
    pointtime = html.xpath('//*[@id="myCalendarTable"]/tbody/tr/td/text()')
    print(pointtime)
    time.sleep(10000)

    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
