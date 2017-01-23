/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.uakron.cesl.weightvisualizerapp;

import com.androidplot.xy.SimpleXYSeries;
import com.androidplot.xy.XYSeries;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author munna
 */
public final class ExponentialFoggsCurveModel extends FoggsCurveModel
{
    
    double[] curveParams = new double[]{0,0,0};
    
    public ExponentialFoggsCurveModel(double[] means) {
        updateCurveParams(means);
    }
    
    @Override
    double getMotivation(double intensity) {
        return Math.exp(curveParams[1]*(intensity + curveParams[0])) + curveParams[2];
    }

    @Override
    double getIntensity(double motivation) {
        return Math.log(motivation - curveParams[2]) / curveParams[1] - curveParams[0];
    }

    @Override
    void updateCurveParams(double[] means) {
        double x1 = means[3];
        double y1 = means[0];
        
        double x2 = 10;
        double y2 = 10;
        double r = means[4];
        double att = means[2];
        
        int N = 100;
        double lamdamin = 0;
        double lamdamax = 2.1;
        // get the midpoint between the two points
        double mx = (x1 + x2) / 2.0;
        double my = (y1 + y2) / 2.0;
        
        // there is a line between this and the point (X2,Y1), find the spot R/8ths along it
        double x3 = mx + 0.5*Math.abs(x2-mx)*(16.0-(r+att))/16.0;
        double y3 = my - 0.5*Math.abs(my-y1)*(16.0-(r+att))/16.0;
        
        // now fit a curve y = A*e^(Bx)+C that matches those three points
        double er, step, lastError, a, b, c;
        step = (lamdamax - lamdamin) / N;
        //A = 0;
        //B = 0;
        //C = 0;
        
        // E^lx
        // E^B(x+A) + C
        
        // big enough so that we won't have any problems
        lastError = Double.MAX_VALUE; 
        //a = 0;
        //b = 0;
        //c = 0;
        for (c = -3; c <= x1; c++) {
            for (a = -10; a < 10; a = a + 0.5) {
                for (b = lamdamin + step; b < lamdamax; b = b + step) {
                    // calculate the error of our ways
                    er = Math.sqrt(Math.pow((Math.exp(b*(x1+a)) + c) - y1, 2) + Math.pow((Math.exp(b*(x2+a)) + c) - y2, 2) + 0.5*Math.pow((Math.exp(b*(x3+a)) + c) - y3, 2));
                    if (er < lastError) {
                        //System.out.println(er + " is less than " + lastError);
                        curveParams[0] = a;
                        curveParams[1] = b;
                        curveParams[2] = c;
                        lastError = er;
                    }
                }
            }
        }
    }

    @Override
    XYSeries getCurve() {
        List<Double> xValues = new ArrayList<>();
        List<Double> yValues = new ArrayList<>();
        for (double intensity = 0; intensity < 10; intensity = intensity + 0.1)
        {
            double motivation = getMotivation(intensity);
            xValues.add(intensity);
            yValues.add(motivation);
        }
        return new SimpleXYSeries(xValues, yValues, "Test1");
    }
    
}
