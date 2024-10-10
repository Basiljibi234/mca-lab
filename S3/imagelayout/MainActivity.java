package com.example.imagelayout;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {
    private ImageView image1, image2, image3;
    private int currentImage = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        image1 = findViewById(R.id.image1);
        image2 = findViewById(R.id.image2);
        image3 = findViewById(R.id.image3);
        Button toggleButton = findViewById(R.id.toggleButton);

        toggleButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                toggleImages();
            }
        });
    }

    private void toggleImages() {
        // Hide all images first
        image1.setVisibility(View.GONE);
        image2.setVisibility(View.GONE);
        image3.setVisibility(View.GONE);

        // Toggle between images
        switch (currentImage) {
            case 1:
                image1.setVisibility(View.VISIBLE);
                currentImage = 2;
                break;
            case 2:
                image2.setVisibility(View.VISIBLE);
                currentImage = 3;
                break;
            case 3:
                image3.setVisibility(View.VISIBLE);
                currentImage = 1;
                break;
        }
    }
}