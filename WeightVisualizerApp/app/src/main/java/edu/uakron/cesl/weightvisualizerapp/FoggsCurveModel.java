/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.uakron.cesl.weightvisualizerapp;

//import org.jfree.data.xy.XYSeries;

import com.androidplot.xy.XYSeries;

/**
 *
 * @author munna
 */
abstract class FoggsCurveModel {
    abstract double getMotivation(double intensity);
    abstract double getIntensity(double motivation);
    abstract void updateCurveParams(double[] newMeans);
    abstract XYSeries getCurve();
    
}
