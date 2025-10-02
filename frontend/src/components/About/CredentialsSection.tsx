import React from "react";
import { GraduationCap, BookOpen } from "lucide-react";

interface CredentialCardProps {
  icon: React.ReactNode;
  title: string;
  institution: string;
  iconBgClass: string;
}

const CredentialCard: React.FC<CredentialCardProps> = ({
  icon,
  title,
  institution,
  iconBgClass,
}) => (
  <div className="bg-white w-full p-6 rounded-xl border border-gray-200/80 shadow-sm transition-shadow hover:shadow-md flex items-start space-x-4">
    <div className={`flex-shrink-0 p-3 rounded-full ${iconBgClass}`}>
      {icon}
    </div>
    <div>
      <h4 className="font-semibold text-gray-800">{title}</h4>
      <p className="text-gray-500">{institution}</p>
    </div>
  </div>
);

const CredentialsSection: React.FC = () => {
  return (
    <section className="py-16 bg-white">
      <div className="container mx-auto px-6 max-w-6xl">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-4">
          About the Founder
        </h2>
        <p className="text-xl text-center text-gray-600 max-w-3xl mx-auto mb-12">
          Meet the mind behind Marjaan Solutions.
        </p>
        <div className="bg-gray-50/80 rounded-2xl p-8 lg:p-12 border border-gray-100">
          <h3 className="text-3xl font-semibold text-blue-700 mb-4">
            Shirdon, Hassen Tahir
          </h3>

          <h3 className="text-2xl font-semibold text-gray-900 mb-4">
            Fullstack Developer & Educator
          </h3>
          <p className="text-gray-600 mb-6 leading-relaxed">
            With hands-on experience in web development, programming, and system
            architecture, our founder has spent years delivering scalable
            solutions for both enterprises and educational institutions. From
            leading development projects at Jeeh General Trading to mentoring
            students and shaping academic programs in Computer Science, we
            combine technical expertise with a deep understanding of operational
            challenges faced by businesses in East Africa.
          </p>

          <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
            <CredentialCard
              icon={<GraduationCap className="h-6 w-6 text-blue-600" />}
              title="Master's in Computational & Cognitive Neuroscience"
              institution="Eötvös Loránd University, Hungary"
              iconBgClass="bg-blue-100"
            />
            <CredentialCard
              icon={<BookOpen className="h-6 w-6 text-green-600" />}
              title="Bachelor's in Computer Science"
              institution="Jigjiga University, Ethiopia"
              iconBgClass="bg-green-100"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default CredentialsSection;
