import React from "react";
import { Target } from "lucide-react";

const MissionStatement: React.FC = () => {
  return (
    <section className="py-20 bg-gray-50">
      <div className="container mx-auto px-6 max-w-6xl text-center">
        <div className="inline-block bg-blue-100 text-blue-600 p-4 rounded-full mb-6">
          <Target className="h-8 w-8" />
        </div>
        <h2 className="text-4xl font-bold text-blue-500 mb-6">Our Mission</h2>
        <p className="text-xl text-gray-700 leading-relaxed font-light max-w-3xl mx-auto">
          "To transform how logistics and transportation companies in East
          Africa manage their daily operations by providing an all-in-one system
          that streamlines HR, finance, and inventory, helping them save time,
          reduce errors, and boost efficiency in an industry where digital
          solutions are scarce."
        </p>
      </div>
    </section>
  );
};

export default MissionStatement;
