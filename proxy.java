public class Proxy{
    public static void main(String[] args) {
        ProxyServer server = new ProxyServer(9978);
        server.start();

        server.addResponseInterceptor(new HttpResponseInterceptor()
        {
            @Override
            public void process(HttpResponse response, HttpContext context)
                throws HttpException, IOException
            {
                System.out.println(response.getStatusLine());
            }
        });

        // Get selenium proxy
        Proxy proxy = server.seleniumProxy();

        // Configure desired capability for using proxy server with WebDriver
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability(CapabilityType.PROXY, proxy);

        // Set up driver
        WebDriver driver = new FirefoxDriver(capabilities);

        driver.get("http://stackoverflow.com/questions/6509628/webdriver-get-http-response-code");

        // Close the browser
        driver.quit();
        <dependency>
           <groupId>net.lightbody.bmp</groupId>
           <artifactId>browsermob-core</artifactId>
           <version>2.1.5</version>
           <scope>test</scope>
       </dependency>
}
