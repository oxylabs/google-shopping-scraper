import okhttp3.*;
import org.json.JSONObject;

public class Main implements Runnable {
    private static final String AUTHORIZATION_HEADER = "Authorization";
    public static final String USERNAME = "YOUR_USERNAME";
    public static final String PASSWORD = "YOUR_PASSWORD";

    public void run() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("source", "google_shopping_product");
        // Get the product token from search results
        jsonObject.put("query", "eyJjYXRhbG9naWQiOiAiODU5MDM3MTQzMDU2NjE1ODI1MiIsICJncGNpZCI6ICIxMDgzMzg0MTk4NjQ2MjAyMTYzMSIsICJpbWFnZURvY2lkIjogIjk1ODcyNDM4NDcwODcwNzM1ODYiLCAibWlkIjogIjU3NjQ2MjUxMTM1NDY1MjkyOSIsICJwdm8iOiAiMTkiLCAicHZ0IjogImEiLCAicmRzIjogIlBDXzEwODMzODQxOTg2NDYyMDIxNjMxfFBST0RfUENfMTA4MzM4NDE5ODY0NjIwMjE2MzEiLCAicHJvZHVjdGlkIjogIiIsICJxdWVyeSI6ICJhZGlkYXMifQ==");
        jsonObject.put("geo_location", "New York,New York,United States");
        jsonObject.put("parse", true);

        Authenticator authenticator = (route, response) -> {
            String credential = Credentials.basic(USERNAME, PASSWORD);

            return response
                    .request()
                    .newBuilder()
                    .header(AUTHORIZATION_HEADER, credential)
                    .build();
        };

        var client = new OkHttpClient.Builder()
                .authenticator(authenticator)
                .build();

        var mediaType = MediaType.parse("application/json; charset=utf-8");
        var body = RequestBody.create(jsonObject.toString(), mediaType);
        var request = new Request.Builder()
                .url("https://realtime.oxylabs.io/v1/queries")
                .post(body)
                .build();

        try (var response = client.newCall(request).execute()) {
            assert response.body() != null;
            System.out.println(response.body().string());
        } catch (Exception exception) {
            System.out.println("Error: " + exception.getMessage());
        }

        System.exit(0);
    }

    public static void main(String[] args) {
        new Thread(new Main()).start();
    }
}