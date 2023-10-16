import frappe
import os
import pyqrcode
import sys
import chilkat2
import OpenSSL
frappe.init(site="husna.erpgulf.com")
frappe.connect()
data = frappe.get_doc("Sales Invoice", "ACC-SINV-2023-00004")
# def create_XML(data):
#     context = {
#         "doc": {
#             "uuid": "123",
#             "posting_date": data.posting_date,
#             "due_date": data.due_date,
#             "company": data.company,
#             "customer": data.customer,
#             "name": data.name,
#             "total": data.total,
#             "tax_id": "123",
#             "company_tax_id": data.tax_category,
#             "pih": "123",
#             "total_taxes_and_charges": data.base_net_total,
#             "company_address_data": {
#                 "street": "20",
#                 "building_no": "1",
#                 "plot_id_no": "1",
#                 "city": "malappuram",
#                 "pincode": "673642",
#                 "state": "pookkottur",
#                 "phone": data.po_no,
#                 "fax": "xthdnd",
#                 "email_id": "@gmail.com"
#             },
#             "shipping_address_data": {
#                 "street": "valluvambram",
#                 "building_no": "3",
#                 "plot_id_no": "7",
#                 "city": "palakkad",
#                 "pincode": "123",
#                 "state": "kerala"
#             },
#             "customer_address_data": {
#                 "street": "valluvambram",
#                 "building_no": "3",
#                 "city": "england",
#                 "pincode": "1245",
#                 "state": "kerala",
#                 "plot_id_no": 2,
#             },
#             "customer_data": {
#                 "street": "valluvambram",
#                 "building_no": "4",
#                 "state": "kerala",
#                 "city": "calicut",
#                 "pincode": "676517",
#                 "tax_id": "1234"
#             },
#             "total": {
#                 "total": data.total,
#             },
#             "grand_total": data.grand_total,
#             "doc": {
#                 "tax_data": {
#                     "total_amount": data.total,
#                 },
#                 "item_meta": {
#                     "tax_amount": data.total_taxes_and_charges,
#                     "total_amount": data.total,
#                     "item.qty": data.total_qty,
#                 },
#                 "e_invoice_items": [
#                     {
#                         "qty": data.total_qty,
#                         "total_amount": data.total_billing_amount,
#                         "tax_amount": data.total_taxes_and_charges,
#                     }],}}}
    
#     template_name = "saudi_phase2_api/saudi_phase2_api/test_rende5.xml"
#     rendered_text = frappe.render_template(template_name, context)
#     # print(rendered_text)
#     encoded_rendered = rendered_text.encode('utf-8')
#     # print(encoded_rendered)
#     doc = frappe.get_doc("Sales Invoice", data.name)
#     filename = f"XML-FOR-{doc.name}.xml".replace(os.path.sep, "__")
#     _file = frappe.get_doc({
#         "doctype": "File",
#         "file_name": filename,
#         # "attached_to_doctype": "Sales Invoice",
#         # "attached_to_name": "ACC-SINV-2023-00004",
#         "file_type": "XML",
#         "content": encoded_rendered,
#         "is_private": 1
#     })
#     try:
#         _file.save()
#     except Exception as e:
#         print("An error occurred:", str(e))
#         pass
#     doc.db_set('custom_xml', _file.file_url, commit=True)
# data = frappe.get_doc("Sales Invoice", "ACC-SINV-2023-00004")
# create_XML(data)

def signXml():
    success = True
    sbXml = chilkat2.StringBuilder()
    success = sbXml.LoadFile("rendered_text", "utf-8")
    if not success:
        print("Failed to load XML file to be signed.")
        sys.exit()
signXml()

#     gen = chilkat2.XmlDSigGen()
#     gen.SigLocation = "Invoice|ext:UBLExtensions|ext:UBLExtension|ext:ExtensionContent|sig:UBLDocumentSignatures|sac:SignatureInformation"
#     gen.SigLocationMod = 0
#     gen.SigId = "signature"
#     gen.SigNamespacePrefix = "ds"
#     gen.SigNamespaceUri = "http://www.w3.org/2000/09/xmldsig#"
#     gen.SignedInfoCanonAlg = "C14N_11"
#     gen.SignedInfoDigestMethod = "sha256"

#     object1 = chilkat2.Xml()
#     object1.Tag = "xades:QualifyingProperties"
#     object1.AddAttribute("xmlns:xades","http://uri.etsi.org/01903/v1.3.2#")
#     object1.AddAttribute("Target","signature")
#     object1.UpdateAttrAt("xades:SignedProperties",True,"Id","xadesSignedProperties")
#     object1.UpdateChildContent("xades:SignedProperties|xades:SignedSignatureProperties|xades:SigningTime","TO BE GENERATED BY CHILKAT")
#     object1.UpdateAttrAt("xades:SignedProperties|xades:SignedSignatureProperties|xades:SigningCertificate|xades:Cert|xades:CertDigest|ds:DigestMethod",True,"Algorithm","http://www.w3.org/2001/04/xmlenc#sha256")
#     object1.UpdateChildContent("xades:SignedProperties|xades:SignedSignatureProperties|xades:SigningCertificate|xades:Cert|xades:CertDigest|ds:DigestValue","TO BE GENERATED BY CHILKAT")
#     object1.UpdateChildContent("xades:SignedProperties|xades:SignedSignatureProperties|xades:SigningCertificate|xades:Cert|xades:IssuerSerial|ds:X509IssuerName","TO BE GENERATED BY CHILKAT")
#     object1.UpdateChildContent("xades:SignedProperties|xades:SignedSignatureProperties|xades:SigningCertificate|xades:Cert|xades:IssuerSerial|ds:X509SerialNumber","TO BE GENERATED BY CHILKAT")

#     gen.AddObject("",object1.GetXml(),"","")

#     xml1 = chilkat2.Xml()
#     xml1.Tag = "ds:Transforms"
#     xml1.UpdateAttrAt("ds:Transform",True,"Algorithm","http://www.w3.org/TR/1999/REC-xpath-19991116")
#     xml1.UpdateChildContent("ds:Transform|ds:XPath","not(//ancestor-or-self::ext:UBLExtensions)")
#     xml1.UpdateAttrAt("ds:Transform[1]",True,"Algorithm","http://www.w3.org/TR/1999/REC-xpath-19991116")
#     xml1.UpdateChildContent("ds:Transform[1]|ds:XPath","not(//ancestor-or-self::cac:Signature)")
#     xml1.UpdateAttrAt("ds:Transform[2]",True,"Algorithm","http://www.w3.org/TR/1999/REC-xpath-19991116")
#     xml1.UpdateChildContent("ds:Transform[2]|ds:XPath","not(//ancestor-or-self::cac:AdditionalDocumentReference[cbc:ID='QR'])")
#     xml1.UpdateAttrAt("ds:Transform[3]",True,"Algorithm","http://www.w3.org/2006/12/xml-c14n11")

#     gen.AddSameDocRef2("","sha256",xml1,"")

#     gen.SetRefIdAttr("","invoiceSignedData")
    
#     gen.AddObjectRef("xadesSignedProperties","sha256","","","http://www.w3.org/2000/09/xmldsig#SignatureProperties")

#     certFromPfx = chilkat2.Cert()
#     success = certFromPfx.LoadPfxFile("/opt/oxy/frappe-bench/apps/saudi_phase2_api/saudi_phase2_api/saudi_phase2_api/test_certi.py","test123")
#     if (success != True):
#         print(certFromPfx.LastErrorText)
#         sys.exit()

#     cert = chilkat2.Cert()
#     success = cert.LoadFromFile("qa_data/zatca/cert.pem")
#     if (success != True):
#         print(cert.LastErrorText)
#         sys.exit()

#     print(cert.SubjectCN)

# # # Load the private key.
# #     privKey = chilkat2.PrivateKey()
# #     success = privKey.LoadPemFile("qa_data/zatca/ec-secp256k1-priv-key.pem")
# #     if (success != True):
# #         print(privKey.LastErrorText)
# #         sys.exit()

# #     print("Key Type: " + privKey.KeyType)

# # # Associate the private key with the certificate.
# #     success = cert.SetPrivateKey(privKey)
# #     if (success != True):
# #         print(cert.LastErrorText)
# #         sys.exit()

# # # The certificate passed to SetX509Cert must have an associated private key.
# # # If the cert was loaded from a PFX, then it should automatically has an associated private key.
# # # If the cert was loaded from PEM, then the private key was explicitly associated as shown above.
# #     success = gen.SetX509Cert(cert,True)
# #     if (success != True):
# #         print(gen.LastErrorText)
# #         sys.exit()

# #     gen.KeyInfoType = "X509Data"
# #     gen.X509Type = "Certificate"

# # # ---------------- This is important -----------------------------------------
# # # Starting in Chilkat v9.5.0.92, add the "ZATCA" behavior to produce the format required by ZATCA.
# #     gen.Behaviors = "IndentedSignature,TransformSignatureXPath,ZATCA"
# # # ----------------------------------------------------------------------------

# # # Sign the XML...
# #     success = gen.CreateXmlDSigSb(sbXml)
# #     if (success != True):
# #         print(gen.LastErrorText)
# #         sys.exit()

# # # -----------------------------------------------

# # # Save the signed XML to a file.
# #     success = sbXml.WriteFile("qa_output/signedXml.xml","utf-8",False)

# #     print(sbXml.GetAsString())

# # # ----------------------------------------
# # # Verify the signatures we just produced...
# #     verifier = chilkat2.XmlDSig()
# #     success = verifier.LoadSignatureSb(sbXml)
# #     if (success != True):
# #         print(verifier.LastErrorText)
# #         sys.exit()

# # # ---------------- This is important -----------------------------------------
# # # Starting in Chilkat v9.5.0.92, specify "ZATCA" in uncommon options 
# # # to validate signed XML according to ZATCA needs.
# # # ----------------------------------------------------------------------------
# #     verifier.UncommonOptions = "ZATCA"

# #     numSigs = verifier.NumSignatures
# #     verifyIdx = 0
# #     while verifyIdx < numSigs :
# #         verifier.Selector = verifyIdx
# #         verified = verifier.VerifySignature(True)
# #         if (verified != True):
# #             print(verifier.LastErrorText)
# #             sys.exit()

# #         verifyIdx = verifyIdx + 1

# #     print("All signatures were successfully verified.")
# # signXml()












# # #     #sing the XML for tag-6
# # #     code for signing xml

# # # def create_QRCode():
# # #     create QTR code 

# # # def sing_XMLsub():
# # #     sub pocerfite








# # # s="encoded_rendered"
# # # url=pyqrcode.create(s)
# # # url.svg("firstqrcode",scale=10)
