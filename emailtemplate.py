f = open('email.txt','r')
message = f.read()
status = message.split(':')
HealthCheck_Status = status[1]
Functional_API_Check = status[3]
Sanity_Tests = status[5]

if HealthCheck_Status == "Stable":
   HealthCheck_Status = "Passed"

if Functional_API_Check == "Stable":
    Functional_API_Check = "Passed"

if Sanity_Tests == "Stable":
    Sanity_Tests = "Passed"



f = open('emailtemplate.html','w')

message = """<html >
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width"/>
 <style>
 * {{ margin: 0; padding: 0; font-size: 100%; font-family: 'Avenir Next', "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; line-height: 1.65; }}
img {{ max-width: 100%; margin: 0 auto; display: block; }}
body, .body-wrap {{ width: 100% !important; height: 100%; background: #f8f8f8; }}
a {{ color: #71bc37; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.text-center {{ text-align: center; }}
.text-right {{ text-align: right; }}
.text-left {{ text-align: left; }}
.button {{ display: inline-block; color: white; background: #71bc37; border: solid #71bc37; border-width: 10px 20px 8px; font-weight: bold; border-radius: 4px; }}
.button:hover {{ text-decoration: none; }}
h1, h2, h3, h4, h5, h6 {{ margin-bottom: 20px; line-height: 1.25; }}
h1 {{ font-size: 32px; }}
h2 {{ font-size: 28px; }}
h3 {{ font-size: 24px; }}
h4 {{ font-size: 20px; }}
h5 {{ font-size: 16px; }}
p, ul, ol {{ font-size: 16px; font-weight: normal; margin-bottom: 20px; }}
.container {{ display: block !important; clear: both !important; margin: 0 auto !important; max-width: 580px !important; }}
.container table {{ width: 100% !important; border-collapse: collapse; }}
.container .masthead {{ padding: 80px 0; background: #71bc37; color: white; }}
.container .masthead h1 {{ margin: 0 auto !important; max-width: 90%; text-transform: uppercase; }}
.container .content {{ background: white; padding: 30px 35px; }}
.container .content.footer {{ background: none; }}
.container .content.footer p {{ margin-bottom: 0; color: #888; text-align: center; font-size: 14px; }}
.container .content.footer a {{ color: #888; text-decoration: none; font-weight: bold; }}
.container .content.footer a:hover {{ text-decoration: underline; }}
.tg  {{border-collapse:collapse;border-spacing:0;border-color:#bbb;}}
.tg td{{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#594F4F;background-color:#E0FFEB;}}
.tg th{{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#493F3F;background-color:#9DE0AD;}}
.tg .tg-imtf{{font-weight:bold;font-size:28px;background-color:#71bc37;color:#ffffff;text-align:center;vertical-align:top}}
.tg .tg-cru3{{font-size:20px;background-color:#ffffff;color:#000000;vertical-align:top}}
.tg .tg-z3b9{{font-weight:bold;font-size:18px;background-color:#ffffff;color:#000000;vertical-align:top}}


    </style>
</head>
<body>
<table class="body-wrap">
    <tr>
        <td class="container">

            <!-- Message start -->
            <table>
                <tr>
                    <td align="center" class="masthead">

                        <h1>TD Insurance Jenkins Report</h1>


                    </td>
                </tr>
                <tr>
                    <td class="content">

                        <h2>Hello Friend,</h2>
                        <h6>Here are the Test Results, your build is: ${{BUILD_STATUS}}</h6>

                        
                        <table>
                            <tr>
                                <td align="center">
                                    <p>
                                        <a href="${{BUILD_URL}}" class="button">Click Here to Go to the Build</a>
                                    </p>
                                </td>
                                <tr>
                                <table class="tg">
								  <tr>
								    <th class="tg-imtf">Test Name</th>
								    <th class="tg-imtf">Results of the Test</th>
								  </tr>
								  <tr>
								    <td class="tg-z3b9">Health Check</td>
								    <td class="tg-cru3">{HealthCheck_Status}</td>
								  </tr>
								  <tr>
								    <td class="tg-z3b9">API Functional Tests</td>
								    <td class="tg-cru3">{Functional_API_Check}</td>
								  </tr>
								  <tr>
								    <td class="tg-z3b9">UI Functional Tests</td>
								    <td class="tg-cru3"> {Sanity_Tests}</td>
								  </tr>
								</table>
								</tr>
                            </tr>
                        </table>

                        <p><center>To unsubscribe from the emails please email the TD Insurance DevOps Team.</center></p>

                        <p><em><center> ~ Your Friend Jenkins</center></em></p>

                    </td>
                </tr>
            </table>

        </td>
    </tr>
</table>
</body>
</html>""".format(HealthCheck_Status =HealthCheck_Status,Functional_API_Check=Functional_API_Check,Sanity_Tests=Sanity_Tests)

f.write(message)
f.close()