import React from "react";
import { Button } from "../ui/button";

const Hero: React.FC = () => {
  return (
    <section className="bg-gradient-to-br from-blue-50 to-indigo-100 py-20">
      <div className="container mx-auto px-6">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            All-in-One Business
            <span className="text-blue-600"> Management</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Streamline your HR, finance, and inventory operations with our
            powerful SaaS platform. Built for modern businesses that scale.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button
              size="lg"
              className="text-lg px-8 py-3 bg-grey-200"
              onClick={() => (window.location.href = "/signup")}
            >
              Start Free Trial
            </Button>
            <Button variant="outline" size="lg" className="text-lg px-8 py-3">
              Watch Demo
            </Button>
          </div>
          <div className="mt-12 bg-white rounded-2xl shadow-xl p-8 border border-gray-200">
            <div className="aspect-video bg-gradient-to-br from-gray-100 to-gray-200 rounded-lg flex items-center justify-center">
              <p className="text-gray-500">Dashboard Preview</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
