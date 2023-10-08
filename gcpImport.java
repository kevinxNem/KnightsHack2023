import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.http.GenericUrl;
import com.google.api.client.http.HttpRequest;
import com.google.api.client.http.HttpResponse;
import com.google.api.client.http.HttpTransport;

public class gcpImport {
    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("API_KEY");
        // Initialize HTTP transport
        HttpTransport httpTransport = GoogleNetHttpTransport.newTrustedTransport();

        // Build the API URL
        GenericUrl url = new GenericUrl("YOUR_API_ENDPOINT_HERE");

        // Build the HTTP request
        HttpRequest request = httpTransport.createRequestFactory().buildGetRequest(url);

        // Add the API key to the request
        request.getUrl().put("key", "YOUR_API_KEY_HERE");

        // Execute the request and handle the response
        HttpResponse response = request.execute();
        String content = response.parseAsString();

        // Use the API response
        System.out.println(content);
    }
}