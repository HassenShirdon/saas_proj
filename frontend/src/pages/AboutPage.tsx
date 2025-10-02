import CredentialsSection from "@/components/About/CredentialsSection";
import MissionStatement from "@/components/About/MissionStatement"; // This path is now correct
import TeamSection from "@/components/About/TeamSection";
import StorySection from "@/components/About/StorySection";
import ValuesSection from "@/components/About/ValuesSection";
import CTASection from "@/components/About/CTASection";

import Footer from "@/components/landing/Footer";
import Header from "@/components/landing/Header";
import Hero from "@/components/landing/Hero";
import React from "react";

const AboutPage = () => {
  return (
    <div className="bg-white">
      <Header />
      <main>
        <Hero />
        <MissionStatement />
        <TeamSection />
        <StorySection />
        <ValuesSection />
        <CredentialsSection />
        <CTASection />
      </main>
      <Footer />
    </div>
  );
};

export default AboutPage;
