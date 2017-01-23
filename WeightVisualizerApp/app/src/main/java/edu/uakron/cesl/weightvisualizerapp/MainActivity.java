package edu.uakron.cesl.weightvisualizerapp;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.SeekBar;

//import com.androidplot.xy.LineAndPointFormatter;
//import com.androidplot.xy.XYPlot;
//import com.androidplot.xy.XYSeriesFormatter;
import com.androidplot.xy.*;
public class MainActivity extends Activity {

    FoggsCurveModel nutritionModel = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        XYPlot plot = (XYPlot) findViewById(R.id.plot_nutrition);
        plot.setPlotMargins(-20, 0, 0, -90);

        double[] means = new double[] {5, 5, 5, 5, 5};
        nutritionModel = new ExponentialFoggsCurveModel(means);

        LineAndPointFormatter formatter = new LineAndPointFormatter(Color.RED, Color.GREEN, null, null);

//        formatter.setInterpolationParams(
//                new CatmullRomInterpolator.Params(10, CatmullRomInterpolator.Type.Centripetal));
        plot.addSeries(nutritionModel.getCurve(), formatter);

        final SeekBar seekbar_nut_intensity = (SeekBar) findViewById(R.id.seekbar_nut_intensity);
        final SeekBar seekbar_nut_motivation = (SeekBar) findViewById(R.id.seekbar_nut_motivation);

        seekbar_nut_intensity.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (fromUser) {
                    Log.e("test", "" + progress + nutritionModel.getMotivation(progress));
                    seekbar_nut_motivation.setProgress((int) nutritionModel.getMotivation(progress));
                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });

        seekbar_nut_motivation.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (fromUser) {
                    Log.e("test", "" + progress + nutritionModel.getIntensity(progress));
                    seekbar_nut_intensity.setProgress((int) nutritionModel.getIntensity(progress));
                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });


//        setSupportActionBar(toolbar);
    }



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
