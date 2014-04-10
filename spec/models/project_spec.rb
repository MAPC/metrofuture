require 'spec_helper'

describe Project do

  before { @project = Project.new(title: "South Coast Rail") }

  subject { @project }

  it { should respond_to :title }
  it { should respond_to :description }
  it { should respond_to :url }
  it { should respond_to :thumbnail }
  it { should respond_to :external_collaborator }
  it { should respond_to :client }
  it { should respond_to :funding_source }
  it { should respond_to :status }
  it { should respond_to :equity_focus }
  it { should respond_to :equity_comment }
  it { should respond_to :start_date }
  it { should respond_to :end_date }

  it { should respond_to :departments }
  it { should respond_to :lead_department }
  it { should respond_to :partner_department }

  it { should respond_to :municipalities }
  it { should respond_to :subregions }

  it { should respond_to :geographies }
  it { should respond_to :display_geographies }

  it { should be_valid }

  describe "when title is blank" do
    before { @project.title = " " }
    it { should_not be_valid }
  end

 describe "when title is too short" do
    before { @project.title = "a" * 2 }
    it { should_not be_valid }
  end 

  describe "when title is too long" do
    before { @project.title = "a" * 171 }
    it { should_not be_valid }
  end
end
