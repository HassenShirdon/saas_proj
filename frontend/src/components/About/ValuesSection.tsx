import React from "react";
import { Zap, Shield, TrendingUp, Target } from "lucide-react";

const ValuesSection: React.FC = () => {
  const values = [
    {
      icon: <Zap className="h-8 w-8 text-blue-600" />,
      title: "Innovation",
      description:
        "Delivering modern solutions tailored for regional business realities.",
    },
    {
      icon: <Shield className="h-8 w-8 text-green-600" />,
      title: "Reliability",
      description: "Systems you can trust to manage critical operations.",
    },
    {
      icon: <TrendingUp className="h-8 w-8 text-purple-600" />,
      title: "Efficiency",
      description: "Automating repetitive tasks to save time and resources.",
    },
    {
      icon: <Target className="h-8 w-8 text-orange-600" />,
      title: "Growth-Driven",
      description: "Helping businesses expand and optimize their processes.",
    },
  ];

  return (
    <section className="py-16 bg-gray-50">
      <div className="container mx-auto px-6 max-w-6xl">
        <h2 className="text-3xl font-bold text-gray-900 mb-12">Our Values</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {values.map((value, index) => (
            <div key={index} className="flex items-start space-x-4">
              <div className="flex-shrink-0 p-3 bg-white rounded-2xl shadow-sm">
                {value.icon}
              </div>
              <div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  {value.title}
                </h3>
                <p className="text-gray-600">{value.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default ValuesSection;
