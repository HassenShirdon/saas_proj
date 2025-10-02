import React from "react";
import Header from "@/components/landing/Header";
import Hero from "@/components/landing/Hero";
import Features from "@/components/landing/Features";
import BenefitsValues from "@/components/landing/BenefitsValues";
import Pricing from "@/components/landing/Pricing";
import Footer from "@/components/landing/Footer";
import FAQSection from "@/components/Landing/FAQSection";
import TestimonialsSection from "@/components/Landing/TestimonialSection";

const LandingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-white">
      <Header />
      <main>
        <Hero />
        <Features />
        <BenefitsValues />
        <FAQSection />
        <TestimonialsSection />
        <Pricing />
      </main>
      <Footer />
    </div>
  );
};

export default LandingPage;
